import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# portfolio returns and volatility
def portf_rtn(w, avg_rtns):
    """
    :param w: weights for different assets/stocks
    :param avg_rtns: the annual average return of different stocks

    :return:portfolio return
    """
    return np.dot(w, avg_rtns)


def portf_vol(w, cov_mat):
    """
    :param w: weights for different assets/stocks
    :param cov_mat: covariance matrix for different stocks

    :return: portfolio volatility
    """
    return np.array([np.sqrt(np.dot(w[i].T, np.dot(cov_mat, w[i]))) for i in range(len(w))])


def mk_portfs(rtns_df):
    """
    make portfolios based on 1 year data simulation
    :param rtns_df: dataframe for stock return

    :return: portfolio volatility and returns dataframe results
    """
    # selected stocks to make your own portfolio
    tickers = input("Do you want to use the above simple returns to make your portfolio? (Y/N)")
    try:
        idx = len(rtns_df[0].iloc[0])
    except:
        idx = len(rtns_df.iloc[0])
    if idx <= 2:
        print("Single asset cannot make a portfolio, please type your new stock tickers to make a portfolio.")
        tickers = 'N'
    # default portfolios parameters
    N_PORTFOLIOS = 10 ** 5  # the number of portfolios simulation
    N_DAYS = 252  # the number of annual trading days

    # calculate average returns and weights for portfolio return and volatility
    if tickers.upper() == 'Y':
        simple_rtns = rtns_df.loc[:, rtns_df.columns.str.contains("simple") == True]
        RISKY_ASSETS = simple_rtns.columns
        years = input("Which year do you want to use to make your portfolio from your previous year input?")
        avg_returns = simple_rtns.loc[years].div(100).mean() * N_DAYS  # divided 100 for no %
        cov_mats = simple_rtns.loc[years].div(100).cov() * N_DAYS
    else:
        stocks = input("Type your own stock tickers to make a new portfolio:")
        RISKY_ASSETS = list(stocks.split(" "))
        years = input("Which year do you want to use to make your portfolio?")
        rtns = yf.download(RISKY_ASSETS, start=f'{years}-01-01', end=f'{years}-12-31')[
            'Adj Close'].pct_change().dropna()
        avg_returns = rtns.mean() * N_DAYS
        cov_mats = rtns.cov() * N_DAYS

    n_assets = len(RISKY_ASSETS)  # number of assets
    # create the portfolio weights
    weights = np.random.random(size=(N_PORTFOLIOS, n_assets))
    weights /= np.sum(weights, axis=1)[:, np.newaxis]

    # calculate the portfolios results (returns, volatility, and sharpe ratio)
    portf_rtns, portf_vols = portf_rtn(weights, avg_returns), portf_vol(weights, cov_mats)
    portf_sharpe_ratio = portf_rtns / portf_vols
    portf_results_df = pd.DataFrame({'returns': portf_rtns,
                                     'volatility': portf_vols,
                                     'sharpe_ratio': portf_sharpe_ratio})

    # print out portfolio performance (maximum sharpe ratio and minimum volatility)
    max_sharpe_ind = np.argmax(portf_results_df.sharpe_ratio)
    max_sharpe_portf = portf_results_df.loc[max_sharpe_ind]

    min_vol_ind = np.argmin(portf_results_df.volatility)
    min_vol_portf = portf_results_df.loc[min_vol_ind]

    print('---- Maximum Sharpe Ratio portfolio ----')
    print('Performance')
    for index, value in max_sharpe_portf.items():
        print(f'{index}: {100 * value:.2f}% ', end="", flush=True)
    print('\nWeights')
    for x, y in zip(RISKY_ASSETS, weights[np.argmax(portf_results_df.sharpe_ratio)]):
        print(f'{x}: {100 * y:.2f}% ', end="", flush=True)

    print('                                         ')
    print('---- Minimum Volatility portfolio ----')
    print('Performance')
    for index, value in min_vol_portf.items():
        print(f'{index}: {100 * value:.2f}% ', end="", flush=True)
    print('\nWeights')
    for x, y in zip(RISKY_ASSETS, weights[np.argmin(portf_results_df.volatility)]):
        print(f'{x}: {100 * y:.2f}% ', end="", flush=True)

    # efficient frontiers plotting
    fig, ax = plt.subplots()
    portf_results_df.plot(kind='scatter', x='volatility',
                          y='returns', c='sharpe_ratio',
                          cmap='RdYlGn', edgecolors='black',
                          ax=ax)
    ax.scatter(x=max_sharpe_portf.volatility,
               y=max_sharpe_portf.returns,
               c='black', marker='*',
               s=200, label='Max Sharpe Ratio')
    ax.scatter(x=min_vol_portf.volatility,
               y=min_vol_portf.returns,
               c='black', marker='P',
               s=200, label='Minimum Volatility')
    ax.set(xlabel='Volatility', ylabel='Expected Returns',
           title='Efficient Frontier')
    ax.legend()
    plt.grid()
    plt.show()

    return portf_results_df
