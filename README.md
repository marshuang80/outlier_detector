# Outlier Detector

A Python application to detect outlier data points in an input CSV file.

The application read the CSV file in, inform the user of the outliers found, and then write a clean version of the data with the outlier points removed. 

## Dependencies
Install relevant dependencies using: 
```
conda env create -f environment.yml
```

## Running the detector
Run the detector using: 
```
python src/main.py --csv_path <path to csv> --col <column name for data>
```

For more argument: 
```
python src/main.py --help 
```

## Development
### Adding more detectors
All new detectors should live in **./src/outlider_detectors.py** as a function. The function will need to take in *df* and *col* as the first two arguments for input dataframe and column name. All other arguments must specify dtype and provide a default value. This will help automatic parsing of function params to argparse arguments. 

Newly added detectors will also need to be specified in outlier_detectors.__all__. This will allow users to choose detectors using input argument.  

### Testing
All new detectors will be accompanied with test cases (see example in **./tests/test_rolling_medium.py)**. All test cases should inherent from TestBase.

