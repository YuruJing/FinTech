import unittest
import pandas as pd
from utils import finance_indicators


class TestInd(unittest.TestCase):
    def test_features(self):
        # single ticker feature extraction
        indicators1 = finance_indicators.extract_features()
        self.assertIsInstance(indicators1, pd.DataFrame)
        self.assertIsNotNone(indicators1)
        # multi tickers feature extraction
        indicators2 = finance_indicators.extract_features()
        self.assertIsInstance(indicators2, pd.DataFrame)
        self.assertIsNotNone(indicators2)


if __name__ != '__main__':
    pass
else:
    unittest.main()
