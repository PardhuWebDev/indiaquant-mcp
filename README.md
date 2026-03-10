IndiaQuant MCP
Developer: Pardha Saradhi CH

This is a Model Context Protocol (MCP) server that provides Claude with real-time access to the Indian Stock Market (NSE). The server integrates live data fetching, quantitative analysis, and a persistent virtual trading environment.

Project Capabilities
The server implements 10 specific tools designed for market analysis and trading:

get_live_price: Real-time NSE data fetching.

get_options_chain: Retrieval of latest calls and puts data.

analyze_sentiment: Volume-based sentiment analysis.

generate_signal: 14-period RSI technical analysis.

get_portfolio_pnl: Real-time P&L tracking for virtual holdings.

place_virtual_trade: Execution of trades via local SQLite storage.

calculate_greeks: Manual Black-Scholes implementation for Delta, Gamma, Theta, and Vega.

detect_unusual_activity: Monitoring for Volume vs. Open Interest anomalies.

scan_market: Technical screening across the Nifty 50.

get_sector_heatmap: Comparative performance analysis of sectoral indices.

Technical Architecture
Mathematical Implementation: Greeks are calculated from scratch using numpy and scipy to demonstrate quantitative reasoning without external libraries.

Modular Design: The project is strictly decoupled into specific modules (market, quant, signals, and portfolio) to ensure maintainability and testability.

Data Persistence: A local SQLite database manages the virtual portfolio, ensuring state is preserved across server restarts.

Infrastructure: Built 100% on free, public APIs to ensure the project remains portable and accessible.

Project Structure
server.py: Entry point for MCP tool registration.

core/market.py: Data ingestion logic.

core/quant.py: Quantitative pricing models.

core/signals.py: Technical indicators and market scanning.

core/portfolio.py: Database management and P&L calculation.

Setup
Install dependencies: pip install mcp yfinance pandas numpy scipy

Update the Claude Desktop configuration to point to the local Python environment and server.py.

Restart Claude Desktop to initialize the tools.
