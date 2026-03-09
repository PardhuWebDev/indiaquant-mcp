# IndiaQuant MCP
**Developer:** Pardhu

### Overview
This is a Model Context Protocol (MCP) server built to connect Claude with the Indian Stock Market (NSE). It allows the AI to fetch live prices, calculate option greeks, and track a virtual portfolio using local Python logic.

### Key Tools
- **Price Checker**: Fetches live NSE stock prices using yfinance.
- **Trend Analysis**: Uses RSI (14-period) to identify Overbought or Oversold stocks.
- **Quant Engine**: Implements the Black-Scholes model for Delta, Gamma, Theta, and Vega.
- **Portfolio Tracker**: Uses SQLite to save trades and calculate live P&L.

### Project Structure
- `server.py`: The main entry point that registers tools for the AI.
- `core/`: 
    - `market.py`: Logic for API data fetching.
    - `quant.py`: Mathematical formulas for options.
    - `signals.py`: Technical analysis indicators.
    - `portfolio.py`: Database management for trades.

### Setup & Installation
1. Install the required libraries:
   `pip install mcp yfinance pandas numpy scipy`

2. Configure Claude Desktop:
   Add the absolute path of `server.py` and your `python.exe` to the Claude `config.json` file.

3. Restart Claude and start asking about NSE stocks!
