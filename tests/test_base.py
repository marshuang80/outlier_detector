"""Base unittest class"""

import unittest
import pandas as pd
import os 
import sys
sys.path.append(os.getcwd())


class TestBase(unittest.TestCase):

    def setUp(self):
        # this is run before every test
        self.df_small = pd.read_csv('./data/gaussian_1d_small.csv')
        self.df = pd.read_csv('./data/gaussian_1d.csv')
        self.col = 'data'


if __name__ == "__main__":
    unittest.main()
