"""A Python application to detect outlier data points in an input CSV file.

The application read the CSV file in, inform the user of the outliers found,
and then write a clean version of the data with the outlier points removed. 
"""

import argparse
import pandas as pd
import outlier_detectors

from utils import add_func_params
        

def main(args: argparse.ArgumentParser):

    # read in input csv file 
    df = pd.read_csv(args.csv_path)

    # remove outlier 
    detector = outlier_detectors.__all__[args.detection_strategy]
    updated_df = detector(
        df, args.column, args.window_size, args.threshold
    )

    # save dataframe to disk
    updated_df.to_csv(args.output_file_path)


if __name__ == '__main__': 

    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--csv_path",
        type=str,
        help="paths to input csv file",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--column",
        type=str,
        help="feature column names",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output_file_path",
        default="no_outlier.csv", 
        type=str,
        help="path to output file with outlier removed",
        required=False,
    )
    parser.add_argument(
        "-d",
        "--detection_strategy",
        default='rolling_median',
        type=str,
        help="strategy for detecting outlier. More information in outlier_detectors.py",
        required=False,
    )
    # add function specfic parameters
    for k, detector in outlier_detectors.__all__.items():
        parser = add_func_params(parser, detector)
    
    # parse args
    args = parser.parse_args()

    main(args)