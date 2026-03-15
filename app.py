import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

from strategy.signals import generate_signals
from backtest.engine import run_backtest
from metrics.performance import calculate_metrics

st.set_page_config(page_title="AI Trading Strategy", layout="wide")

st.title("AI-Assisted Intraday Trading Strategy Dashboard")

ticker = "QQQ"

data = yf.download(ticker, period="7d", interval="5m")

data = generate_signals(data)
data = run_backtest(data)
metrics = calculate_metrics(data)

st.subheader("Price Chart with Signals")

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(data.index, data["Close"], label="Close Price")
ax.plot(data.index, data["ma20"], label="MA20")

buy = data[data["signal"] == 1]
sell = data[data["signal"] == -1]

ax.scatter(buy.index, buy["Close"], marker="^", label="Buy")
ax.scatter(sell.index, sell["Close"], marker="v", label="Sell")

ax.legend()
ax.grid(True)

st.pyplot(fig)

st.subheader("Cumulative Return")

fig2, ax2 = plt.subplots()
ax2.plot(data.index, data["cum_return"])
ax2.grid(True)

st.pyplot(fig2)

st.subheader("Performance Metrics")

for k,v in metrics.items():
    st.write(k, ":", v)