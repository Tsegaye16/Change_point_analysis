import pandas as pd
import gdown
import os
from IPython.display import display  # Import display for better output in notebooks
import logging

class DataPreprocessor:
    def __init__(self,logger: logging.Logger = None):
        """
        Initialize the DataPreprocessor class with the Google Drive link to the dataset.
        
        Parameters:
        drive_link (str): The Google Drive shareable link to the data file.
        output_dir (str): The directory where the data file will be saved.
        output_file (str): The local file name to save the downloaded data.
        logger (logging.Logger): Logger for tracking events and errors.
        """
        
        #self.file_path = file_path
        self.data: pd.DataFrame = None
        self.logger = logger if logger else logging.getLogger(__name__)

    def load_data(self, file_path) -> pd.DataFrame:
        """
        Load the dataset from Google Drive, save it in the specified directory,
        and read it into a pandas DataFrame.
        
        Returns:
        pd.DataFrame: The loaded dataset.
        """
        try:
           
            
         

            # Load data into a pandas DataFrame
            self.data = pd.read_csv(file_path)
            # Convert Date to Datetime format
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='mixed', errors='coerce')
            self.data.set_index('Date', inplace=True)

            self.logger.info("Data loaded into DataFrame successfully.")
            return self.data
        
        except Exception as e:
            self.logger.error(f"Error loading data: {e}")
            raise


    def inspect(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Inspect the given DataFrame for structure, completeness, and summary statistics.

        Parameters:
        - df (pd.DataFrame): The DataFrame to inspect.

        Returns:
        - pd.DataFrame: Summary statistics for numeric columns.
        """
        if df.empty:
            raise ValueError("The DataFrame is empty.")

        try:
            # Check and display the dimensions of the DataFrame
            df = df.reset_index()
            dimensions = df.shape
            print(f"Dimensions (rows, columns): {dimensions}")
            self.logger.info(f"DataFrame dimensions: {dimensions}")

            # Check and display data types of each column
            data_types = df.dtypes
            print("\nData Types:")
            print(data_types)
            self.logger.info("Displayed data types for each column.")

            # Check for missing values in each column
            missing_values = df.isnull().sum()
            if missing_values.any():
                print("\nMissing Values:")
                print(missing_values[missing_values > 0])
                self.logger.warning("Missing values found.")
            else:
                print("\nNo missing values found.")
                self.logger.info("No missing values detected.")

            # Check and display the count of unique values for each column
            unique_values = df.nunique()
            print("\nUnique Values in Each Column:")
            print(unique_values)
            
            # Count the number of duplicate rows
            duplicate_count = df.duplicated().sum()
            print(f"Number of duplicate rows: {duplicate_count}")
            self.logger.info(f"Duplicate rows found: {duplicate_count}")

            # View duplicate rows if any
            if duplicate_count > 0:
                duplicates = df[df.duplicated()]
                print("Duplicate rows:")
                print(duplicates)


            # Summary statistics for numeric columns
            summary_statistics = df.describe(include='number')
            print("\nSummary Statistics for Numeric Columns:")
            display(summary_statistics)  # Display as a DataFrame
            
            # return summary_statistics  # Return for further use if needed

        except Exception as e:
            self.logger.error(f"An error occurred while inspecting the dataset: {e}")
            raise