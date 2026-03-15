def analyze_trend(df):
    df = df.copy()

    close = df["Close"]
    ma20 = close.rolling(20).mean()
    ma50 = close.rolling(50).mean()

    latest_close = float(close.iloc[-1])
    latest_ma20 = float(ma20.iloc[-1]) if not ma20.isna().iloc[-1] else latest_close
    latest_ma50 = float(ma50.iloc[-1]) if not ma50.isna().iloc[-1] else latest_close

    if latest_close > latest_ma20 > latest_ma50:
        trend = "Bullish"
        score = 2
    elif latest_close < latest_ma20 < latest_ma50:
        trend = "Bearish"
        score = -2
    else:
        trend = "Neutral"
        score = 0

    distance_ma20 = ((latest_close - latest_ma20) / latest_ma20) if latest_ma20 != 0 else 0.0

    return {
        "trend": trend,
        "trend_score": score,
        "latest_close": latest_close,
        "ma20": latest_ma20,
        "ma50": latest_ma50,
        "distance_to_ma20": float(distance_ma20)
    }
