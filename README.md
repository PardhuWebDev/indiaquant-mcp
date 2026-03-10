IndiaQuant MCP
Developer: Pardha Saradhi CH

This project is a Model Context Protocol (MCP) server that integrates real-time Indian Stock Market (NSE) intelligence into Claude Desktop. It allows an AI assistant to perform live data retrieval, quantitative analysis, and virtual portfolio management.

Features
The server exposes 10 specialized tools for financial analysis:

Market Data: Live price fetching and sector performance heatmaps.

Options Analytics: Real-time options chain retrieval and unusual activity detection (Volume vs. OI spikes).

Quant Engine: From-scratch Black-Scholes implementation for Delta, Gamma, Theta, and Vega.

Technical Signals: 14-period RSI trend detection and market-wide scanning for "Buy" setups.

Virtual Trading: Persistent SQLite-backed portfolio tracking with real-time P&L calculation.

Technical Decisions
Mathematical Implementation: To demonstrate quantitative reasoning, Option Greeks are calculated manually using numpy and scipy rather than external pricing libraries.

Modular Architecture: The codebase is decoupled into logic-specific modules (market, quant, signals, portfolio) for better maintainability.

Sentiment Proxy: Due to API constraints, sentiment is derived from volume-weighted price action, identifying high-interest stocks without requiring paid news feeds.

Project Structure
server.py: Main entry point for tool registration.

core/market.py: Handles API interactions with yfinance.

core/quant.py: Contains Black-Scholes mathematical models.

core/signals.py: Technical indicators and screening logic.

core/portfolio.py: Manages database persistence and wallet logic.
