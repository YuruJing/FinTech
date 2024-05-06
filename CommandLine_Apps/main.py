import pandas as pd
from utils import get_stocks, plotting, portfolio, finance_indicators
import fire


# # create my apps
def MyApp():
    # check get sp500 or not
    check1 = input("Do you want to check sp500 companies tickers (Y/N)?")
    if check1.upper() == 'Y':
        get_stocks.get_stock_tickers()

    print("I will here to help you scrape stock price data, calculate stock returns and make basic plots!")
    stock_price = get_stocks.get_stock_price()
    stock_returns = get_stocks.stock_rtns(stock_price)
    print(stock_returns)

    # check plot regression or not
    check2 = input("Do you want to check regression plots (Y/N)?")
    if check2.upper() == 'Y':
        if isinstance(stock_returns, pd.DataFrame):
            plotting.reg_plot(stock_returns)

        else:
            stock_rtns, stats = stock_returns[0], stock_returns[1]
            plotting.reg_plot(stock_rtns)

    finance_dict = {'portfolios': [], 'indicators': []}  # store financial dataframes
    # check make a portfolio or not
    check3 = input("Do you want to make a portfolio or not (Y/N)?")
    if check3.upper() == 'Y':
        try:
            port = portfolio.mk_portfs(stock_returns)
        except:
            port = portfolio.mk_portfs(stock_rtns)
        finance_dict['portfolios'] = port

    print('\n')
    # check extract financial indicators or not
    check4 = input("Do you want to get financial indicators (Y/N)?")
    if check4.upper() == 'Y':
        fin_indicators = finance_indicators.extract_features()
        finance_dict['indicators'] = fin_indicators
        print(fin_indicators)  # could add extra identification to adjust parameters

    print("Thank you for using my app! End current Myapps Enquires' functionalities!")
    print("New functionality will be added soon!")

    # return stock_returns, finance_dict


if __name__ == "__main__":
    fire.Fire(MyApp)
