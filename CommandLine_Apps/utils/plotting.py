import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import pandas as pd
import numpy as np


# check regression between all selected stock and all benchmarks
def reg_plot(stock_returns):
    """
    :param stock_returns: Dataframe for stock returns (simple and log returns)

    :return: all stock returns (benchmarks and selected stocks)
    """
    # download benchmark adjusted close prices
    benchmarks = yf.download(['SPY', 'BND', 'GLD', 'QQQ', 'VTI'], start=stock_returns.index[0], end=stock_returns.index[-1])['Adj Close']
    bench_log = []

    # calculate benchmark stock returns
    for b in benchmarks.columns:
        benchmarks['{}_simple_rtn'.format(b)] = benchmarks[b].pct_change().mul(100)
        benchmarks['{}_log_rtn'.format(b)] = np.log(benchmarks[b] / benchmarks[b].shift(1)).mul(100)
        bench_log.append('{}_log_rtn'.format(b))

    # drop benchmark price columns
    benchmarks.drop(columns=['SPY', 'BND', 'GLD', 'QQQ', 'VTI'], inplace=True)

    # regression relationship between benchmarks and selected stock log returns
    df = pd.concat([stock_returns, benchmarks], axis=1)
    df.dropna(inplace=True)  # drop NA

    # create regression plots
    for col in stock_returns.columns:
        if 'log' in col:
            for blog in bench_log:
                rho = df[col].corr(df[blog])  # correlation of coefficient
                sns.regplot(x=col, y=blog, data=df, fit_reg=True, label=f'{blog}($\\rho$ = {rho:.2f})')
            plt.title(f'{col} vs. benchmarks')
            plt.xlabel(f'{col} log returns')
            plt.ylabel('Benchmarks log returns')
            plt.legend()
            plt.grid()
            plt.show()

    return df  # all returns
