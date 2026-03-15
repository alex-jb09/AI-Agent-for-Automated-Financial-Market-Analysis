import pandas as pd

def calculate_rsi(data, period=14):
    delta = data["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_signals(df):
    df = df.copy()

    df["ma20"] = df["Close"].rolling(20).mean()
    df["RSI"] = calculate_rsi(df)

    df["signal"] = 0

    buy_condition = (df["Close"] < df["ma20"]) & (df["RSI"] < 30)
    sell_condition = (df["Close"] > df["ma20"]) & (df["RSI"] > 70)

    df.loc[buy_condition, "signal"] = 1
    df.loc[sell_condition, "signal"] = -1

    return df