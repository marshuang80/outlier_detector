"""testcases for rolling median"""

import unittest
import os 
import sys
sys.path.append(os.getcwd())

from src.outlier_detectors import rolling_median
from tests.test_base import TestBase

class TestBase(TestBase):

    def test_check_small_w10_thres_std(self):
        """check outlier results on small dataset with window_size=5 and 
        threshold=None
        """

        df = rolling_median(self.df_small, self.col, 10, None)
        self.assertTrue(len(df) == 18)

    def test_check_small_w10_thres_05(self):
        """check outlier results on small dataset with window_size=5 and 
        threshold=None
        """

        df = rolling_median(self.df_small, self.col, 10, 0.5)
        self.assertTrue(len(df) == 18)

    def test_check_w10_thres_std(self):
        """check outlier results on small dataset with window_size=5 and 
        threshold=None
        """

        df = rolling_median(self.df, self.col, 10, None)
        self.assertTrue(len(df) == 450)

    def test_check_w10_thres_05(self):
        """check outlier results on dataset with window_size=5 and 
        threshold=None
        """

        df = rolling_median(self.df, self.col, 10, 0.5)
        self.assertTrue(len(df) == 991)


if __name__ == "__main__":
    unittest.main()