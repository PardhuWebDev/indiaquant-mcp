import yfinance as yf

class Market:
    def format_symbol(self, symbol: str):
        symbol = symbol.upper().strip()
        if not (symbol.endswith(".NS") or symbol.endswith(".BO")):
            return f"{symbol}.NS"
        return symbol

    def get_live(self, symbol: str):
        name = self.format_symbol(symbol)
        t = yf.Ticker(name)
        info = t.fast_info
        return {
            "symbol": name,
            "price": round(info['last_price'], 2),
            "volume": info['last_volume']
        }

    def get_history(self, symbol: str):
        name = self.format_symbol(symbol)
        return yf.Ticker(name).history(period="1mo")