# 🪙 XRP Arbitrage Trading Bot

## 📌 Overview

The **XRP Arbitrage Trading Bot** is a Python-based automated trading bot designed to identify and execute arbitrage opportunities for XRP across multiple cryptocurrency exchanges. The bot fetches real-time pricing data, validates potential trades, and executes profitable trades while accounting for trading fees.

---

## 🚀 Features

- **📡 Real-Time Data Collection**  
  Fetches XRP prices from multiple exchanges using the `ccxt` library.

- **📊 Arbitrage Validation**  
  Identifies arbitrage opportunities based on price differences between exchanges.

- **🤖 Automated Trading**  
  Executes trades automatically when profitable opportunities are found.

- **💰 Profit Tracking**  
  Tracks total profit and logs successful trades to a local SQLite database.

- **⚙️ Customizable Parameters**  
  - `TRADE_DIFFERENCE`: Minimum price difference required to execute a trade.
  - `FEE`: Trading fee percentage (applied to both buy and sell trades).
  - `Trading Hours`: Operates only during specified trading hours (07:00 to 22:00 SAST).
  - `Keyboard Interrupt`: Allows manual termination of the bot using the `q` key.

---

## 🛠 Requirements

### ✅ Python Version

- Python 3.8 or higher

### 📦 Python Libraries

Install the required libraries using:

```bash
pip install ccxt pytz colorama
