import pandas as pd

class Signals:
    def check_rsi(self, symbol: str):
        from core.market import Market
        m = Market()
        df = m.get_history(symbol)
        
        if len(df) < 15:
            return "Need more data"
            
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        last_rsi = rsi.iloc[-1]
        
        if last_rsi > 70: return "OVERBOUGHT"
        elif last_rsi < 30: return "OVERSOLD"
        else: return "NEUTRAL"