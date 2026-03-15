import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

from signals import generate_signals
from engine import run_backtest
from performance import calculate_metrics
from trend_analysis import analyze_trend
from watchlist import analyze_watchlist
from ai_summary import generate_ai_summary

st.set_page_config(page_title="AI Trading Final Project Prototype", layout="wide")

st.title("AI Agent for Short-Term Financial Market Analysis")
st.write(
    "Final project prototype: market data + technical indicators + trend analysis + watchlist ranking + AI summary."
)

st.sidebar.header("Settings")

ticker = st.sidebar.selectbox(
    "Select Ticker",
    ["QQQ", "SPY", "AAPL", "TSLA", "NVDA", "MSFT", "META", "AMZN"],
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

watchlist_input = st.sidebar.text_input(
    "Watchlist (comma separated)",
    "QQQ, SPY, AAPL, TSLA, NVDA"
)

st.sidebar.markdown("### Strategy Rules")
st.sidebar.write("Buy when:")
st.sidebar.write("- Price < MA20")
st.sidebar.write("- RSI < 30")
st.sidebar.write("Sell when:")
st.sidebar.write("- Price > MA20")
st.sidebar.write("- RSI > 70")

data = yf.download(ticker, period=period, interval=interval, auto_adjust=False, progress=False)

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data = data.dropna().copy()

if data.empty:
    st.error("No data was downloaded. Please try another ticker or interval.")
    st.stop()

data = generate_signals(data)
data = run_backtest(data)
data["market_return"] = data["Close"].pct_change()
data["market_cum_return"] = (1 + data["market_return"].fillna(0)).cumprod()

metrics = calculate_metrics(data)
trend_info = analyze_trend(data)

latest_signal = int(data["signal"].iloc[-1])
latest_rsi = float(data["RSI"].iloc[-1])

summary = generate_ai_summary(ticker, trend_info, latest_signal, latest_rsi, metrics)

st.subheader(f"{ticker} Market Snapshot")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Trend", trend_info["trend"])
c2.metric("Latest Close", f"{trend_info['latest_close']:.2f}")
c3.metric("RSI", f"{latest_rsi:.2f}")
c4.metric("Signal", str(latest_signal))
c5.metric("MA20 Distance", f"{trend_info['distance_to_ma20']:.2%}")

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

st.subheader("Performance Metrics")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Return", f"{metrics['Total Return']:.2%}")
m2.metric("Sharpe Ratio", f"{metrics['Sharpe Ratio']:.2f}")
m3.metric("Max Drawdown", f"{metrics['Max Drawdown']:.2%}")
m4.metric("Number of Trades", int(metrics["Number of Trades"]))

st.subheader("AI Summary")
st.write(summary)

st.subheader("Watchlist Ranking")
tickers = [x.strip().upper() for x in watchlist_input.split(",") if x.strip()]
watchlist_df = analyze_watchlist(tickers, period=period, interval=interval)
st.dataframe(watchlist_df, use_container_width=True)

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
st.dataframe(data[available_columns].tail(20), use_container_width=True)

st.subheader("Project Notes")
st.write(
    '''
    - This is a final-project-ready prototype for AI-assisted short-term market analysis.
    - The current version uses market data and technical indicators.
    - The next upgrade can add financial news sentiment and LLM-based market commentary.
    - This structure can later be extended into a browser extension, plugin, or paper trading assistant.
    '''
)
