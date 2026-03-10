import yfinance as yf

class Market:
    def clean(self, s):
        s = s.upper()
        return s if (".NS" in s or ".BO" in s) else s + ".NS"

    def get_live(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        return {"price": round(t.fast_info['last_price'], 2), "vol": t.fast_info['last_volume']}

    def get_options(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        if not t.options: return "No options"
        chain = t.option_chain(t.options[0])
        return chain.calls.nlargest(5, 'volume')[['strike', 'lastPrice', 'volume', 'openInterest']].to_dict()

    def unusual_oi(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        chain = t.option_chain(t.options[0]).calls
        # Spike detection: Volume > Open Interest
        spikes = chain[chain['volume'] > chain['openInterest']]
        return spikes[['strike', 'volume', 'openInterest']].to_dict() if not spikes.empty else "No spikes"

    def sectors(self):
        idx = {"BANK": "^NSEBANK", "IT": "^CNXIT", "AUTO": "^CNXAUTO"}
        res = {}
        for k, v in idx.items():
            h = yf.Ticker(v).history(period="2d")
            change = ((h['Close'].iloc[-1] - h['Close'].iloc[-2]) / h['Close'].iloc[-2]) * 100
            res[k] = f"{round(change, 2)}%"
        return res
