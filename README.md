# AI-Assisted Intraday Trading Strategy

# AI-Assisted Intraday Trading Strategy

This project demonstrates how AI-assisted tools can be used to design and evaluate algorithmic trading strategies using financial market data.

The system downloads market data from Yahoo Finance, generates trading signals using technical indicators, and evaluates strategy performance through backtesting.

---

## Strategy Logic

The strategy uses a simple mean reversion approach based on:

- Moving Average (MA20)
- Relative Strength Index (RSI)

Buy signal:
- Price < MA20
- RSI < 30

Sell signal:
- Price > MA20
- RSI > 70

---

## Features

- Interactive trading dashboard using Streamlit
- Real-time market data via Yahoo Finance API
- Technical indicator based signal generation
- Strategy backtesting engine
- Strategy vs Buy-and-Hold comparison
- Performance metrics including:
  - Total Return
  - Sharpe Ratio
  - Max Drawdown
  - Number of Trades

---

## Run the Project

Install dependencies:

