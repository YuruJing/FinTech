import unittest
from utils import get_stocks, portfolio


class TestPortf(unittest.TestCase):
    def test_portf(self):
        price = get_stocks.get_stock_price()
        rtn = get_stocks.stock_rtns(price)
        with self.assertRaises(Exception):
            portfolio.mk_portfs(rtn)


if __name__ != '__main__':
    pass
else:
    unittest.main()