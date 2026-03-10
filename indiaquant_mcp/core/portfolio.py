import sqlite3
import os

class Portfolio:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(os.path.dirname(base), "portfolio.db")
        with sqlite3.connect(self.db) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS stocks (symbol TEXT PRIMARY KEY, qty INT, price REAL)")
            conn.execute("CREATE TABLE IF NOT EXISTS wallet (id INT PRIMARY KEY, bal REAL)")
            conn.execute("INSERT OR IGNORE INTO wallet VALUES (1, 1000000.0)")

    def add(self, symbol, qty, price, side):
        with sqlite3.connect(self.db) as conn:
            if side.lower() == 'buy':
                cost = qty * price
                conn.execute("UPDATE wallet SET bal = bal - ? WHERE id = 1", (cost,))
                conn.execute("INSERT INTO stocks VALUES (?,?,?) ON CONFLICT(symbol) DO UPDATE SET price=(price*qty+?)/(qty+?), qty=qty+?", 
                             (symbol.upper(), qty, price, (price*qty), qty, qty))
                return f"Bought {qty} {symbol}"
        return "Trade processed"

    def status(self, market_instance):
        with sqlite3.connect(self.db) as conn:
            rows = conn.execute("SELECT * FROM stocks").fetchall()
            pnl = 0
            for s, q, p in rows:
                live = market_instance.get_live(s)['price']
                pnl += (live - p) * q
            return {"total_pnl": round(pnl, 2), "holdings": len(rows)}
