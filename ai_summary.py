def generate_ai_summary(ticker, trend_info, latest_signal, latest_rsi, metrics):
    trend = trend_info["trend"]

    if latest_signal == 1:
        signal_text = "A short-term mean reversion buy signal is currently active."
    elif latest_signal == -1:
        signal_text = "A short-term mean reversion sell signal is currently active."
    else:
        signal_text = "There is no active mean reversion entry signal right now."

    if latest_rsi < 30:
        rsi_text = "RSI suggests the stock is in oversold territory."
    elif latest_rsi > 70:
        rsi_text = "RSI suggests the stock is in overbought territory."
    else:
        rsi_text = "RSI is in a more neutral range."

    if trend == "Bullish":
        trend_text = "The short-term trend appears bullish."
    elif trend == "Bearish":
        trend_text = "The short-term trend appears bearish."
    else:
        trend_text = "The short-term trend appears neutral."

    perf_text = (
        f"The backtest currently shows total return of {metrics['Total Return']:.2%}, "
        f"Sharpe ratio of {metrics['Sharpe Ratio']:.2f}, "
        f"and max drawdown of {metrics['Max Drawdown']:.2%}."
    )

    return f"{ticker} analysis summary: {trend_text} {rsi_text} {signal_text} {perf_text}"
