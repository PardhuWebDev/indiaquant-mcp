import sqlite3
import os

class Portfolio:
    def __init__(self):
        root = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(os.path.dirname(root), "portfolio.db")
        self.setup()

    def setup(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS positions (symbol TEXT PRIMARY KEY, qty INT, price REAL)")
            conn.execute("CREATE TABLE IF NOT EXISTS wallet (id INT PRIMARY KEY, bal REAL)")
            conn.execute("INSERT OR IGNORE INTO wallet VALUES (1, 1000000.0)")

    def place_trade(self, symbol, qty, price, side):
        symbol = symbol.upper()
        with sqlite3.connect(self.db_path) as conn:
            if side.lower() == 'buy':
                val = qty * price
                conn.execute("UPDATE wallet SET bal = bal - ? WHERE id = 1", (val,))
                conn.execute("INSERT INTO positions VALUES (?,?,?) ON CONFLICT(symbol) DO UPDATE SET price=(price*qty+?)/(qty+?), qty=qty+?", 
                             (symbol, qty, price, (price*qty), qty, qty))
                return "done"
        return "error"

    def get_portfolio_status(self, feed):
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute("SELECT * FROM positions").fetchall()
            res = []
            for s, q, p in rows:
                now = feed.get(s, p)
                diff = (now - p) * q
                res.append({"stock": s, "shares": q, "pnl": round(diff, 2)})
            return res