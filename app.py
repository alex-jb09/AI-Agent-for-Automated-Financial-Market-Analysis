import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

from signals import generate_signals
from engine import run_backtest
from performance import calculate_metrics

st.set_page_config(page_title="AI Trading Strategy", layout="wide")

st.title("AI-Assisted Intraday Trading Strategy Dashboard")
st.write("This dashboard demonstrates an intraday mean reversion trading strategy using market data and technical indicators.")

# Sidebar controls
st.sidebar.header("Settings")

ticker = st.sidebar.selectbox(
    "Select Ticker",
    ["QQQ", "SPY", "AAPL", "TSLA", "NVDA"],
    index=0
)

period = st.sidebar.selectbox(
    "Select Data Period",
    ["5d", "7d", "1mo"],
    index=1
)

interval = st.sidebar.selectbox(
    "Select Interval",
    ["5m", "15m", "30m"],
    index=0
)

st.sidebar.markdown("### Strategy Rules")
st.sidebar.write("Buy when:")
st.sidebar.write("- Price < MA20")
st.sidebar.write("- RSI < 30")
st.sidebar.write("Sell when:")
st.sidebar.write("- Price > MA20")
st.sidebar.write("- RSI > 70")

# Load data
data = yf.download(ticker, period=period, interval=interval, auto_adjust=False)

# Fix possible multi-level columns from yfinance
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data = data.dropna().copy()

if data.empty:
    st.error("No data was downloaded. Please try another ticker or interval.")
    st.stop()

# Generate signals and backtest
data = generate_signals(data)
data = run_backtest(data)

# Market benchmark return
data["market_return"] = data["Close"].pct_change()
data["market_cum_return"] = (1 + data["market_return"].fillna(0)).cumprod()

metrics = calculate_metrics(data)

# Show raw columns for debugging if needed
with st.expander("Show Raw Data Columns"):
    st.write(list(data.columns))

# Price chart with signals
st.subheader(f"{ticker} Price Chart with Trading Signals")

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(data.index, data["Close"], label="Close Price")
ax.plot(data.index, data["ma20"], label="MA20")

buy = data[data["signal"] == 1]
sell = data[data["signal"] == -1]

ax.scatter(buy.index, buy["Close"], marker="^", s=80, label="Buy Signal")
ax.scatter(sell.index, sell["Close"], marker="v", s=80, label="Sell Signal")

ax.set_title(f"{ticker} Price and Trading Signals")
ax.set_xlabel("Time")
ax.set_ylabel("Price")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Strategy vs Market comparison
st.subheader("Strategy vs Buy-and-Hold Performance")

fig2, ax2 = plt.subplots(figsize=(14, 5))
ax2.plot(data.index, data["cum_return"], label="Strategy Return")
ax2.plot(data.index, data["market_cum_return"], label="Buy and Hold Return")

ax2.set_title("Cumulative Returns Comparison")
ax2.set_xlabel("Time")
ax2.set_ylabel("Cumulative Return")
ax2.legend()
ax2.grid(True)

st.pyplot(fig2)

# Performance metrics
st.subheader("Performance Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Return", f"{metrics['Total Return']:.2%}")
col2.metric("Sharpe Ratio", f"{metrics['Sharpe Ratio']:.2f}")
col3.metric("Max Drawdown", f"{metrics['Max Drawdown']:.2%}")
col4.metric("Number of Trades", int(metrics["Number of Trades"]))

# Recent data table
st.subheader("Recent Strategy Data")

display_columns = [
    "Close",
    "ma20",
    "RSI",
    "signal",
    "return",
    "strategy_return",
    "cum_return",
    "market_cum_return"
]

available_columns = [col for col in display_columns if col in data.columns]

st.dataframe(data[available_columns].tail(20))

# Project notes
st.subheader("Project Notes")
st.write(
    """
    - This project implements an intraday mean reversion trading strategy.
    - The strategy uses a 20-period moving average and RSI to generate buy and sell signals.
    - Buy signals are generated when price is below MA20 and RSI indicates oversold conditions.
    - Sell signals are generated when price is above MA20 and RSI indicates overbought conditions.
    - The strategy is compared against a simple buy-and-hold benchmark.
    - This project is part of a broader AI Agent for Automated Financial Market Analysis system.
    """
)
