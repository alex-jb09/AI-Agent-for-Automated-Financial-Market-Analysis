# AI Agent for Short-Term Financial Market Analysis

This project implements an AI-assisted trading strategy analysis system for short-term financial markets.  
The system collects market data, generates trading signals using technical indicators, evaluates strategy performance, and visualizes results through an interactive dashboard.

The goal of the project is to demonstrate how programming paradigms and data analysis techniques can be applied to financial market analysis.

---

# Project Overview

Financial markets generate a large amount of data every day. Retail investors often struggle to quickly interpret market signals and identify potential trading opportunities.

This project builds a prototype **AI trading assistant** that:

• Collects historical stock market data  
• Computes technical indicators  
• Generates trading signals  
• Backtests the trading strategy  
• Visualizes results in an interactive dashboard  

The system allows users to analyze multiple stocks and evaluate short-term trading strategies.

---

# Trading Strategy

The strategy uses two common technical indicators:

**Moving Average (MA20)**  
Represents the short-term trend of the stock price.

**Relative Strength Index (RSI)**  
Measures momentum and overbought / oversold conditions.

### Buy Condition
- Price < MA20  
- RSI < 30  

### Sell Condition
- Price > MA20  
- RSI > 70  

This strategy attempts to identify short-term reversal opportunities in the market.

---

# System Architecture

The system is composed of several modules:

Market Data Module  
→ Downloads intraday stock data from Yahoo Finance.

Technical Indicator Module  
→ Computes indicators such as MA20 and RSI.

Signal Generation Module  
→ Generates buy and sell signals based on strategy rules.

Backtesting Engine  
→ Simulates trading and calculates strategy performance.

Performance Evaluation  
→ Computes financial metrics such as Sharpe ratio and drawdown.

Dashboard Interface  
→ Visualizes market data, signals, and performance metrics using Streamlit.

---

# Dashboard Features

The Streamlit dashboard provides an interactive interface that allows users to:

• Select stock tickers  
• Choose data period and time interval  
• View price charts with trading signals  
• Compare strategy performance with buy-and-hold  
• Analyze multiple stocks using a watchlist  

The dashboard also displays key performance metrics including:

- Total Return
- Sharpe Ratio
- Maximum Drawdown
- Number of Trades

---

# Example Dashboard Output

The dashboard includes:

• Price chart with buy/sell signals  
• Strategy vs Buy-and-Hold comparison  
• Performance metrics  
• Recent strategy data table  

This allows users to visually evaluate how the strategy performs over time.

---

# Technologies Used

Python  
Pandas  
NumPy  
Matplotlib  
Streamlit  
Yahoo Finance API (yfinance)

---

# How to Run the Project

Clone the repository:

```bash
git clone https://github.com/alex-jb09/AI-Agent-for-Automated-Financial-Market-Analysis.git
```

Navigate to the project folder:

```bash
cd AI-Agent-for-Automated-Financial-Market-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
python -m streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# Performance Metrics

The strategy is evaluated using several financial metrics:

**Total Return**  
Measures the overall profitability of the strategy.

**Sharpe Ratio**  
Evaluates risk-adjusted return.

**Maximum Drawdown**  
Measures the largest peak-to-trough loss.

**Number of Trades**  
Indicates how frequently the strategy executes trades.

These metrics allow comparison between the trading strategy and a buy-and-hold baseline.

---

# Future Improvements

Future versions of the system may include:

• Financial news sentiment analysis  
• AI-generated market commentary  
• Support and resistance detection  
• Trade opportunity ranking  
• Real-time alerts for trading signals  
• Browser extension for market analysis

These enhancements would transform the system into a more advanced **AI trading assistant**.

---

# Author

Xiaoyu Ji  
Computer Science Graduate Student  
Yeshiva University

---

# License

This project is for educational purposes.
