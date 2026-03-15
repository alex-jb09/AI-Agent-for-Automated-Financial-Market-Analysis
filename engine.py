def run_backtest(df):
    df = df.copy()

    df["return"] = df["Close"].pct_change()
    df["strategy_return"] = df["signal"].shift(1) * df["return"]
    df["cum_return"] = (1 + df["strategy_return"].fillna(0)).cumprod()

    return df
