import numpy as np

def calculate_metrics(df):
    strategy_returns = df["strategy_return"].dropna()

    total_return = df["cum_return"].iloc[-1] - 1

    if strategy_returns.std() == 0 or len(strategy_returns) == 0:
        sharpe = 0.0
    else:
        sharpe = np.sqrt(252) * strategy_returns.mean() / strategy_returns.std()

    drawdown = df["cum_return"] / df["cum_return"].cummax() - 1
    max_drawdown = drawdown.min()

    trades = (df["signal"].diff().fillna(0) != 0).sum()

    return {
        "Total Return": total_return,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_drawdown,
        "Number of Trades": trades
    }