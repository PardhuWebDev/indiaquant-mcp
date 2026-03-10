import yfinance as yf

class Market:
    def clean(self, s):
        s = s.upper()
        if ".NS" not in s and ".BO" not in s:
            return s + ".NS"
        return s

    def get_live(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        info = t.fast_info
        return {"price": round(info['last_price'], 2), "vol": info['last_volume']}

    def get_options(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        if not t.options: return "No data"
        chain = t.option_chain(t.options[0])
        return chain.calls.nlargest(5, 'volume')[['strike', 'lastPrice', 'volume', 'openInterest']].to_dict()

    def unusual_oi(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        if not t.options: return "No options found"
        chain = t.option_chain(t.options[0]).calls
        # Detect where Volume > Open Interest
        spikes = chain[chain['volume'] > chain['openInterest']]
        if spikes.empty: return "No unusual volume detected"
        return spikes[['strike', 'volume', 'openInterest']].to_dict()

    def sectors(self):
        # Tracking Nifty Sector Indices
        idx = {"BANK": "^NSEBANK", "IT": "^CNXIT", "AUTO": "^CNXAUTO", "METAL": "^CNXMETAL"}
        res = {}
        for k, v in idx.items():
            h = yf.Ticker(v).history(period="2d")
            chg = ((h['Close'].iloc[-1] - h['Close'].iloc[-2]) / h['Close'].iloc[-2]) * 100
            res[k] = f"{round(chg, 2)}%"
        return res
