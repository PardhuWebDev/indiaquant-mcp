import pandas as pd
import yfinance as yf
from core.market import Market

class Signals:
    def get_signal(self, symbol):
        m = Market()
        t = yf.Ticker(m.clean(symbol))
        df = t.history(period="1mo")
        if len(df) < 15: return "HOLD"
        
        diff = df['Close'].diff()
        u = diff.where(diff > 0, 0).rolling(14).mean()
        d = -diff.where(diff < 0, 0).rolling(14).mean()
        rsi = 100 - (100 / (1 + (u/d))).iloc[-1]
        
        if rsi > 70: return "SELL"
        if rsi < 30: return "BUY"
        return "HOLD"

    def get_sentiment(self, symbol):
        m = Market()
        t = yf.Ticker(m.clean(symbol))
        h = t.history(period="5d")
        if h['Volume'].iloc[-1] > h['Volume'].mean() * 1.5:
            return "Positive Sentiment (High Volume)"
        return "Neutral"

    def scanner(self):
        watch = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "SBIN.NS"]
        buys = [s for s in watch if self.get_signal(s) == "BUY"]
        return buys if buys else "No Buy signals currently"
