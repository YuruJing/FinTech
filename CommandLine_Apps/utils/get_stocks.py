import yfinance as yf
import pandas as pd
import numpy as np
import scipy.stats as scs
from datetime import date
import matplotlib.pyplot as plt


# get sp500 companies stock tickers (uses as benchmarks, 80% market capitalization, investors will considered)   will
# further investigate randomly company tickers enquire
def get_stock_tickers():
    """
    get sp500 companies stock tickers
    """
    print('Enquire Table: List of all S&P 500 companies with their matched stock tickers.')
    sp500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

    sp500_tickers.rename(columns={'Symbol': 'Tickers', 'Security': 'Company Name'}, inplace=True)
    print(sp500_tickers)

    return sp500_tickers


# get the stock price
def get_stock_price():
    """
    default (Y/N): return to benchmark stock price or not
    default Y to enquire benchmarks today's stock price
    default N to customized your stock price retrival

    return: stock adjusted close price
    """
    # choose the retrieve modes
    default = input(
        'type Y to retrieve today benchmark stock prices, type N to customize your own stock price retrieval):')

    # default mode to retrieve today benchmark stock prices
    if default.upper() == 'Y':
        print('You are in the default mode!')
        tickers = ['SPY', 'BND', 'GLD', 'QQQ', 'VTI']
        start = date.today()
        end = None

    # customized mode to retrieve your own
    else:
        print('You are in the customized mode!')
        print('                                                                           ')
        # print description to avoid the users get errors to retrieve stock data
        print('Multiple stock tickers needs to be separate by space/comma when you type!!!')
        print('-------------------------------------------------------------------------')
        print('Start/End date input should be as format like 2010-01-01')
        print('-------------------------------------------------------------------------')

        # input tickers and date want to retrieve
        tickers = input('Type single/multiple stock tickers you want to retrieve:')
        start = input('Type start date you want to enquire (if only want to price of today, type T):')
        if start.upper() == 'T':  # today's price only
            start = date.today()
            end = None

        else:
            end = input('Type end date you want to enquire: ')

    stock_price = yf.download(tickers, start=start, end=end)['Adj Close']  # retrieve stock data
    if isinstance(stock_price, pd.DataFrame):
        return stock_price
    else:
        return stock_price.to_frame(tickers.upper())


# calculate stock returns
def stock_rtns(stock_price):
    """
    :param stock_price: adjusted close stock price from func: get_stock_price

    :return: simple and log returns of stock price
    """
    # stock price needs to drop later
    drop_columns = stock_price.columns

    # calculate stock returns (simple and log)
    for i in drop_columns:
        stock_price['{}_simple_rtn'.format(i)] = stock_price[i].pct_change().mul(100)
        stock_price['{}_log_rtn'.format(i)] = np.log(stock_price[i] / stock_price[i].shift(1)).mul(100)

    # drop NA and stock price columns
    stock_price.dropna(inplace=True)
    stock_price.drop(columns=drop_columns, axis=1, inplace=True)

    # user interactive: calculate descriptive statistics or not
    rtn_stats = input('Do you want to check descriptive statistics for all stock returns?(Y/N)')
    # descriptive statistics for stock returns
    if rtn_stats.upper() == 'Y':
        # create a statistics descriptive dataframe table
        stats_index = ['Range of dates', 'No. of observations', 'Mean', 'Median',
                       'Min', 'Max', 'Standard Deviation', 'Skewness', 'Kurtosis', 'Jarque-Bera statistic',
                       'Jarque-Bera P-value']
        desp = pd.DataFrame(columns=list(stock_price.columns), index=stats_index)

        print('---------- Descriptive Statistics ----------')
        for j in desp.columns:
            jbtest = scs.jarque_bera(stock_price[j])
            desp[j] = ['{} to {}'.format(min(stock_price.index.date), max(stock_price.index.date)),
                       stock_price[j].shape[0], round(stock_price[j].mean(), 4),
                       round(stock_price[j].median(), 4), round(stock_price[j].min(), 4),
                       round(stock_price[j].max(), 4), round(stock_price[j].std(), 4),
                       round(stock_price[j].skew(), 4), round(stock_price[j].kurtosis(), 4), round(jbtest[0], 4),
                       round(jbtest[1], 4)]
        print(desp)

    # plotting stock check
    stock_plot = input('Do you want to show stock plots? (Y/N)')
    if stock_plot.upper() == 'Y':
        # stock return plots
        stock_price.plot()
        plt.grid()
        plt.legend(loc='upper right')
        plt.xlabel('date')
        plt.ylabel('stock simple/log return(%)')
        plt.title('stock returns')

        # moving average/volatility plots
        window = input('Please type window size (integer) for moving average and volatility:')
        stock_price.rolling(window=int(window)).agg(['mean', 'std']).plot()
        plt.grid()
        plt.legend(loc='upper right')
        plt.xlabel('date')
        plt.ylabel(f'stock return {window} days moving average/volatility(%)')
        plt.title('Moving stock returns')
        plt.show()

    try:
        return stock_price, desp  # get stock returns and statistics descriptive
    except:
        return stock_price  # get stock returns
