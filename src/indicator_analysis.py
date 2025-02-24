# data_processing.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import wbdata

# Set default figure size for all plots
plt.rcParams['figure.figsize'] = (14, 7)

# Define indicator codes
INDICATORS = {
    'GDP': 'NY.GDP.MKTP.CD',                # GDP (current US$)
    'CPI': 'FP.CPI.TOTL.ZG',                # Inflation (CPI)
    'Unemployment Rate': 'SL.UEM.TOTL.ZS',  # Unemployment rate (% of total labor force)
    'Exchange Rate': 'PA.NUS.FCRF'          # Exchange rate, USD to other currencies
}

# Function to fetch data from World Bank
def fetch_data(indicator_code, indicator_name, country='WLD', start_date=None, end_date=None):
    """Fetches data from World Bank Data for a specified indicator."""
    data = wbdata.get_dataframe({indicator_code: indicator_name}, country=country, date=(start_date, end_date))
    return data

# Function to clean data
def clean_data(df, indicator_name):
    """Cleans the DataFrame by resetting index, renaming columns, and handling missing values."""
    if df is not None and not df.empty:
        df.reset_index(inplace=True)
        df.columns = ['date', indicator_name]  # Rename columns
        df.dropna(inplace=True)
        df['date'] = pd.to_datetime(df['date'])
        return df
    return pd.DataFrame()  # Return an empty DataFrame if input is None or empty

# Function to convert data to daily frequency
def convert_to_daily(df, date_col='date'):
    """Converts a DataFrame with dates to a daily frequency."""
    full_index = pd.date_range(start=df[date_col].min(), end=df[date_col].max(), freq='D')
    df_daily = df.set_index(date_col).reindex(full_index)
    df_daily.interpolate(method='time', inplace=True)  # Interpolate to fill missing values
    df_daily.reset_index(inplace=True)
    df_daily.rename(columns={'index': 'Date'}, inplace=True)
    return df_daily

# Function to fetch, clean, and save data
def process_indicator(indicator_code, indicator_name, country='WLD', start_date=None, end_date=None):
    """Fetches, cleans, and saves data for a given indicator."""
    data = fetch_data(indicator_code, indicator_name, country, start_date, end_date)
    cleaned_data = clean_data(data, indicator_name)
    daily_data = convert_to_daily(cleaned_data)
    daily_data.to_csv(f"../data/{indicator_name}_cleaned_data_daily.csv", index=False)
    return daily_data

# Function to analyze and visualize correlations
def analyze_and_visualize(indicator_data, indicator_name, oil_data, x_label):
    """
    Analyzes the correlation between an indicator and oil prices,
    and generates a scatter plot.
    """
    merged_data = pd.merge(indicator_data, oil_data.reset_index(), on='Date')
    merged_data.dropna(inplace=True)  # Drop NaN values for correlation calculation
    correlation = merged_data[indicator_name].corr(merged_data['Price'])
    print(f"Correlation between {indicator_name} and oil prices: {correlation}")

    # Scatter plot
    plt.figure(figsize=(10, 4))
    sns.scatterplot(data=merged_data, x=indicator_name, y='Price')
    plt.title(f'{indicator_name} vs Brent Oil Prices')
    plt.xlabel(x_label)
    plt.ylabel('Brent Oil Price ($)')
    plt.show()

# Function to merge all datasets
def merge_datasets(datasets):
    """Merges multiple datasets on the 'Date' column."""
    merged_data = datasets[0]
    for dataset in datasets[1:]:
        merged_data = merged_data.merge(dataset, on='Date', how='outer')
    merged_data.ffill(inplace=True)  # Forward fill missing values
    return merged_data

# Function to visualize correlation heatmap
def visualize_correlation_heatmap(data):
    """Visualizes the correlation matrix as a heatmap."""
    plt.figure(figsize=(10, 6))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Economic Indicators and Oil Prices')
    plt.show()

# Function to plot time series of indicators and oil prices
def plot_time_series(data, x_col, y_cols, title):
    """Plots time series data for multiple columns."""
    plt.figure(figsize=(14, 7))
    for y_col in y_cols:
        sns.lineplot(data=data, x=x_col, y=y_col, label=y_col)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# Function to plot distributions of indicators and oil prices
def plot_distributions(data, columns):
    """Plots distribution plots for specified columns."""
    plt.figure(figsize=(14, 7))
    for col in columns:
        sns.histplot(data[col], kde=True, label=col)
    plt.title('Distribution of Indicators and Oil Prices')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

# Function to plot rolling averages
def plot_rolling_averages(data, x_col, y_cols, window=30, title='Rolling Averages'):
    """Plots rolling averages for specified columns."""
    plt.figure(figsize=(14, 7))
    for y_col in y_cols:
        data[f'{y_col}_rolling'] = data[y_col].rolling(window=window).mean()
        sns.lineplot(data=data, x=x_col, y=f'{y_col}_rolling', label=f'{y_col} (Rolling Avg)')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# Function to plot pair plots
def plot_pair_plots(data, columns):
    """Plots pair plots for specified columns."""
    sns.pairplot(data[columns])
    plt.suptitle('Pair Plots of Indicators and Oil Prices', y=1.02)
    plt.show()