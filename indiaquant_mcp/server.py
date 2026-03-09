import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcp.server.fastmcp import FastMCP
from core.market import Market
from core.quant import Quant
from core.signals import Signals
from core.portfolio import Portfolio

mcp = FastMCP("indiaquant")
m_logic = Market()
q_logic = Quant()
s_logic = Signals()
p_logic = Portfolio()

@mcp.tool()
def get_price(symbol: str):
    return m_logic.get_live(symbol)

@mcp.tool()
def calculate_greeks(price: float, strike: float, days: int, vol: float):
    return q_logic.get_greeks(price, strike, days, vol, 0.07)

@mcp.tool()
def check_trend(symbol: str):
    return s_logic.check_rsi(symbol)

@mcp.tool()
def place_order(symbol: str, qty: int, price: float, side: str):
    return p_logic.place_trade(symbol, qty, price, side)

@mcp.tool()
def show_portfolio():
    data = m_logic.get_live("RELIANCE.NS")
    return p_logic.get_portfolio_status({"RELIANCE.NS": data['price']})

if __name__ == "__main__":
    mcp.run()