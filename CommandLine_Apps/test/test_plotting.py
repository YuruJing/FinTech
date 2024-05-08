import unittest
from utils import plotting, get_stocks


class TestPlot(unittest.TestCase):
    def test_plot(self):
        price = get_stocks.get_stock_price()
        rtn = get_stocks.stock_rtns(price)
        with self.assertRaises(Exception):
            plotting.reg_plot(rtn)


if __name__ != '__main__':
    pass
else:
    unittest.main()

