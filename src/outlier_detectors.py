"""Outlier detector functions used in main"""

import numpy as np
import argparse
import pandas as pd


def rolling_median(
        df: pd.DataFrame, col:str, window_size:int=5, threshold:float=None
    ) -> pd.DataFrame: 
    """Detect outlier in a stream of data using a rolling window. 

    An instances is considered as an outlier if it is more than +/- threshold 
    from the window median.

    Args: 
        df (pd.DataFrame): pandas Dataframe with input datastream
        col (str): column name of input datastream
        window_size (int): size of the rolling window
        threshold (float): the threshold for outlier. Any instance greater than 
            median + threshold or less than median - threshold is considered as 
            an outlier. By default, the threshold is computed as the 2 std of
            the given window.

    Returns: 
        A pandas Dataframe with outlier removed
    """

    # list for storing outlier index 
    outlier_idx = []

    # ensure dataframe index is in order 
    df = df.reset_index()

    # stream input data
    for start_idx in range(0, len(df)-window_size+1):

        # window level information
        window = df.iloc[start_idx: start_idx+window_size]
        window_values = window[col]
        window_median = np.median(window_values)
        window_diff = window_values - window_median

        # set threshold        
        if threshold is None: 
            thres = np.std(window_values)
        else: 
            thres = threshold

        # find outlier 
        outliers = window_diff[
            (window_diff > thres) | (window_diff < - thres)
        ]
        outlier_idx += outliers.index.tolist()

    # drop rows with outliers
    df = df.drop(outlier_idx)

    return df


__all__ = {
    'rolling_median': rolling_median,
}