import yfinance as yf

class Market:
    def clean(self, s):
        s = s.upper()
        return s if (".NS" in s or ".BO" in s) else s + ".NS"

    def get_live(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        h = t.history(period="2d")
        if len(h) < 2: return {"error": "data unavailable"}
        
        price = h['Close'].iloc[-1]
        prev_price = h['Close'].iloc[-2]
        change_pct = ((price - prev_price) / prev_price) * 100
        
        return {
            "price": round(price, 2),
            "change%": f"{round(change_pct, 2)}%",
            "volume": int(h['Volume'].iloc[-1])
        }

    def get_options(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        if not t.options: return "No options data"
        chain = t.option_chain(t.options[0])
        return chain.calls.nlargest(5, 'openInterest')[['strike', 'lastPrice', 'openInterest']].to_dict()

    def unusual_oi(self, symbol):
        t = yf.Ticker(self.clean(symbol))
        if not t.options: return "No anomalies"
        chain = t.option_chain(t.options[0]).calls
        spikes = chain[chain['volume'] > (chain['openInterest'] * 1.2)]
        return spikes[['strike', 'volume', 'openInterest']].to_dict() if not spikes.empty else "No spikes"

    def sectors(self):
        idx = {"BANK": "^NSEBANK", "IT": "^CNXIT", "AUTO": "^CNXAUTO"}
        res = {}
        for k, v in idx.items():
            h = yf.Ticker(v).history(period="2d")
            chg = ((h['Close'].iloc[-1] - h['Close'].iloc[-2]) / h['Close'].iloc[-2]) * 100
            res[k] = f"{round(chg, 2)}%"
        return res
