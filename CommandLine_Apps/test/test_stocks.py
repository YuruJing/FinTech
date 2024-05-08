import unittest
import pandas as pd
from utils import get_stocks


class TestStock(unittest.TestCase):
    def test_tickers(self):
        tickers = get_stocks.get_stock_tickers()
        self.assertIsInstance(tickers, pd.DataFrame)
        self.assertTrue(len(tickers) >= 500)

    def test_price(self):
        # try default mode (type Y)
        price1 = get_stocks.get_stock_price()
        self.assertIsInstance(price1, pd.DataFrame)
        self.assertTrue(price1.shape == (1, 5))
        # try customized mode with single ticker today price (type N, aapl, T)
        price2 = get_stocks.get_stock_price()
        self.assertIsInstance(price2, pd.DataFrame)
        self.assertIsNotNone(price2)
        self.assertTrue(price2.shape == (1, 1))
        # try customized mode with multi tickers today price (type N, (aapl,msft,amd), T)
        price3 = get_stocks.get_stock_price()
        self.assertIsInstance(price3, pd.DataFrame)
        self.assertIsNotNone(price3)
        self.assertTrue(price3.shape == (1, 3))
        # try customized mode with single ticker in date range (type N, (aapl), date range)
        price4 = get_stocks.get_stock_price()
        self.assertIsInstance(price4, pd.DataFrame)
        self.assertIsNotNone(price4)
        self.assertTrue(price4.shape == (len(price4), 1))
        # try customized mode with multi tickers in date range (type N, (aapl,msft,amd), date range)
        price5 = get_stocks.get_stock_price()
        self.assertIsInstance(price5, pd.DataFrame)
        self.assertIsNotNone(price5)
        self.assertTrue(price4.shape == (len(price5), 3))

    def test_returns(self):
        # test single ticker case without descriptive statistics (type N for stats)
        single_price = get_stocks.get_stock_price()  #(type N, (aapl), date range)
        return1 = get_stocks.stock_rtns(single_price)
        self.assertIsInstance(return1, pd.DataFrame)
        self.assertIsNotNone(return1)
        self.assertTrue(return1.shape == (len(return1, 2)))
        # test single ticker case with descriptive statistics (type Y for stats)
        self.assertIsInstance(return1, tuple)
        self.assertIsNotNone(return1[1])
        # test multi tickers case without descriptive statistics (type N for stats)
        multi_price = get_stocks.get_stock_price()  # (type N, (aapl,msft,amd), date range)
        return2 = get_stocks.stock_rtns(multi_price)
        self.assertIsInstance(return2, pd.DataFrame)
        self.assertIsNotNone(return2)
        self.assertTrue(return2.shape == (len(return2, 6)))
        # test single ticker case with descriptive statistics (type Y for stats)
        self.assertIsInstance(return2, tuple)
        self.assertIsNotNone(return2[1])


if __name__ != '__main__':
    pass
else:
    unittest.main()
