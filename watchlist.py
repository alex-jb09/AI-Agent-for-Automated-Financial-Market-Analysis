import pandas as pd
import yfinance as yf

from signals import generate_signals
from trend_analysis import analyze_trend

def _normalize_columns(df):
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df

def analyze_watchlist(tickers, period="7d", interval="5m"):
    results = []

    for ticker in tickers:
        try:
            df = yf.download(ticker, period=period, interval=interval, auto_adjust=False, progress=False)
            df = _normalize_columns(df).dropna().copy()

            if df.empty or len(df) < 60:
                continue

            df = generate_signals(df)
            trend_info = analyze_trend(df)

            latest = df.iloc[-1]
            latest_signal = int(latest["signal"])
            latest_rsi = float(latest["RSI"])
            latest_close = float(latest["Close"])
            latest_ma20 = float(latest["ma20"])

            setup_score = 0

            if trend_info["trend"] == "Bullish":
                setup_score += 2
            elif trend_info["trend"] == "Bearish":
                setup_score -= 2

            if latest_signal == 1:
                setup_score += 2
            elif latest_signal == -1:
                setup_score -= 2

            if latest_rsi < 30:
                setup_score += 1
            elif latest_rsi > 70:
                setup_score -= 1

            results.append({
                "Ticker": ticker,
                "Trend": trend_info["trend"],
                "Signal": latest_signal,
                "RSI": round(latest_rsi, 2),
                "Close": round(latest_close, 2),
                "MA20": round(latest_ma20, 2),
                "Setup Score": setup_score
            })
        except Exception:
            continue

    if not results:
        return pd.DataFrame(columns=["Ticker", "Trend", "Signal", "RSI", "Close", "MA20", "Setup Score"])

    out = pd.DataFrame(results).sort_values(by="Setup Score", ascending=False).reset_index(drop=True)
    return out
