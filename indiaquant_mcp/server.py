import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcp.server.fastmcp import FastMCP
from core.market import Market
from core.quant import Quant
from core.signals import Signals
from core.portfolio import Portfolio

mcp = FastMCP("indiaquant")
m = Market()
q = Quant()
s = Signals()
p = Portfolio()

@mcp.tool()
def get_live_price(symbol: str):
    return m.get_live(symbol)

@mcp.tool()
def get_options_chain(symbol: str):
    return m.get_options(symbol)

@mcp.tool()
def analyze_sentiment(symbol: str):
    return s.get_sentiment(symbol)

@mcp.tool()
def generate_signal(symbol: str):
    return s.get_signal(symbol)

@mcp.tool()
def get_portfolio_pnl():
    return p.status(m)

@mcp.tool()
def place_virtual_trade(symbol: str, qty: int, price: float, side: str):
    return p.add(symbol, qty, price, side)

@mcp.tool()
def calculate_greeks(S: float, K: float, days: int, vol: float):
    return q.calculate(S, K, days, vol, 0.07)

@mcp.tool()
def detect_unusual_activity(symbol: str):
    return m.unusual_oi(symbol)

@mcp.tool()
def scan_market():
    return s.scanner()

@mcp.tool()
def get_sector_heatmap():
    return m.sectors()

if __name__ == "__main__":
    mcp.run()
