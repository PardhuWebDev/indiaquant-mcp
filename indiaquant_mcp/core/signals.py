import yfinance as yf
from core.market import Market

class Signals:
    def get_signal(self, symbol):
        m = Market()
        df = yf.Ticker(m.clean(symbol)).history(period="1mo")
        if len(df) < 15: return {"signal": "HOLD", "confidence": "0%"}
        
        diff = df['Close'].diff()
        u = diff.where(diff > 0, 0).rolling(14).mean()
        d = -diff.where(diff < 0, 0).rolling(14).mean()
        rsi = 100 - (100 / (1 + (u/d))).iloc[-1]
    
        conf = abs(rsi - 50) * 2 
        
        sig = "HOLD"
        if rsi > 70: sig = "SELL"
        elif rsi < 30: sig = "BUY"
        
        return {"signal": sig, "confidence": f"{round(conf, 1)}%"}

    def get_sentiment(self, symbol):
        t = yf.Ticker(Market().clean(symbol))
        h = t.history(period="5d")
        score = 50 # Neutral
        if h['Volume'].iloc[-1] > h['Volume'].mean() * 1.5: score = 85
        return {"score": score, "signal": "BULLISH" if score > 50 else "NEUTRAL"}

    def scanner(self):
        watch = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS"]
        return [s for s in watch if self.get_signal(s)['signal'] == "BUY"]
