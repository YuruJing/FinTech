import pandas as pd
import yfinance as yf


# simple moving average and volatility (for closing/adj closing only usually)
def MAV(price, size):
    """
    :param price: dataframe of stock price
    :param size: sliding window size for the moving

    :return: moving average and volatility for stock adjusted close price
    """
    col = price.columns.get_level_values(0).unique().to_list()
    if len(col) == 1:
        price = price[col[0]]
        new_columns = [(col[0], 'mean'), (col[0], 'std')]
        df = price['Adj Close'].rolling(size).agg(['mean', 'std'])
        df.columns = pd.MultiIndex.from_tuples(new_columns)
        return df

    return price['Adj Close'].rolling(size).agg(['mean', 'std'])


# relative strength index
def RSI(price, size):
    """
    :param price: dataframe of stock price
    :param size: sliding window size for the moving

    :return rsi: relative strength index
    """
    # get the stock tickers
    col = price.columns.get_level_values(0).unique().to_list()
    if len(col) == 1:
        price = price[col[0]]
        delta = price['Adj Close'].diff().to_frame(col[0])  # difference between current price and previous price
    else:
        delta = price['Adj Close'].diff()  # difference between current price and previous price

    # get price increase days and price decrease days
    delta_up, delta_down = delta[delta > 0], delta[delta < 0]

    # calculate relative strength and relative strength index
    rs = delta_up.ewm(alpha=1 / size, min_periods=size).mean() / abs(
        delta_down.ewm(alpha=1 / size, min_periods=size).mean())
    rsi = 100 - 100 / (1 + rs)

    # relative strength index by different stocks
    new_columns = [(i, 'RSI') for i in rsi.columns]
    rsi.columns = pd.MultiIndex.from_tuples(new_columns)
    return rsi


# MACD: Moving Average Convergence Divergence
def MACD(price, slow_ema=12, fast_ema=26):
    """
    :param price: dataframe  of stock price
    :param slow_ema: a shorter period of ema (period days)
    :param fast_ema: a longer period of ema (period days)

    :return macd: Moving Average Convergence Divergence
    """
    col = price.columns.get_level_values(0).unique().to_list()
    if len(col) == 1:
        price = price[col[0]]
        # Calculate the exponential moving averages (EMA)
        ema_slow = price['Adj Close'].ewm(span=slow_ema, min_periods=slow_ema - 1, adjust=False).mean()
        ema_fast = price['Adj Close'].ewm(span=fast_ema, min_periods=fast_ema - 1, adjust=False).mean()
        macd = ema_fast - ema_slow  # moving average convergence divergence
        macd = macd.to_frame(col[0])
    else:
        # Calculate the exponential moving averages (EMA)
        ema_slow = price['Adj Close'].ewm(span=slow_ema, min_periods=slow_ema - 1, adjust=False).mean()
        ema_fast = price['Adj Close'].ewm(span=fast_ema, min_periods=fast_ema - 1, adjust=False).mean()
        macd = ema_fast - ema_slow  # moving average convergence divergence

    # moving average convergence divergence by different stocks
    new_columns = pd.MultiIndex.from_tuples([(i, 'MACD') for i in macd.columns])
    macd.columns = new_columns

    return macd


# extract features: prices with financial indicators
def extract_features(ma_size=40, rsi_size=12, slow_ema=12, fast_ema=26):
    """
    :param ma_size: sliding window size for the moving average/volatility calculation
    :param rsi_size: sliding window size for the relative strength index calculation
    :param slow_ema: a shorter period of ema (period days)
    :param fast_ema: a longer period of ema (period days)

    :return all_features: all features output
    """
    # print description to avoid the users get errors to retrieve stock data
    print('Multiple stock tickers needs to be separate by space/comma when you type!!!')
    print('-------------------------------------------------------------------------')
    print('Start/End date input should be as format like 2010-01-01')
    print('-------------------------------------------------------------------------')
    # input tickers and date want to retrieve
    tickers = input('Type single/multiple stock tickers you want to retrieve:')
    start = input('Type start date you want to enquire:')
    end = input('Type end date you want to enquire:')
    # download finance data
    data = yf.download(tickers, start=start, end=end)

    if len(data.columns[0]) == 2:
        swap_data = data.swaplevel(axis=1)  # swap columns level

    else:
        data.columns = pd.MultiIndex.from_tuples([(tickers.upper(), i) for i in data.columns])
        swap_data = data

    columns = swap_data.columns.get_level_values(0).unique().to_list()  # get unique stock tickers

    # calculate features: combine stock prices with all financial indicators
    com_features = pd.concat([swap_data, MAV(data, ma_size), RSI(data, rsi_size), MACD(data, slow_ema, fast_ema)], axis=1)
    for c in columns:
        com_features[(c, 'return')] = com_features[c]['Adj Close'].pct_change().mul(100)

    all_features = com_features.dropna()
    return all_features



