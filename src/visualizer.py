
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import IPython.display as display
from IPython.display import HTML

class DataVisualizer:
    def __init__(self, data: pd.DataFrame, logger):
        """
        Initialize the DataVisualizer with data and a logger instance.
        
        Parameters:
        - data (pd.DataFrame): DataFrame containing 'Date' and 'Price' columns.
        - logger: Logger instance for logging events and errors.
        """
        self.data = data
        self.logger = logger
        self.logger.info("DataVisualizer initialized.")

        
        
    def _display_error_message(self, method_name):
            """Displays an error message with a hyperlink to the log file in the notebook."""
            log_link = f'<a href="../logs/notebooks.log" target="_blank">Check the log file for details</a>'
            display.display(HTML(f"<p style='color:red;'>An error occurred in {method_name}. {log_link}</p>"))

    def plot_box(self):
        """Plots a box plot of Brent Oil Prices."""
        try:
            plt.figure(figsize=(8, 4))
            sns.boxplot(data=self.data, y='Price')
            plt.title('Box Plot of Brent Oil Prices')
            plt.ylabel('Price (USD per barrel)')
            plt.show()
            self.logger.info("Box plot of Brent Oil Prices displayed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to plot box plot: {e}")
            self._display_error_message("plot_boxplot")

    def plot_price_over_time(self):
        """Plots Brent Oil Prices over time."""
        try:
            plt.figure(figsize=(10, 4))
            plt.plot(self.data.index, self.data['Price'], label='Brent Oil Price', color='blue')
            plt.title('Brent Oil Prices Over Time')
            plt.xlabel('Date')
            plt.ylabel('Price (USD per barrel)')
            plt.legend()
            plt.show()
            self.logger.info("Price over time plot displayed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to plot price over time: {e}")
            self._display_error_message("plot_price_over_time")

    def plot_price_distribution(self):
        """Plots the distribution of Brent Oil Prices."""
        try:
            plt.figure(figsize=(10, 4))
            sns.histplot(self.data['Price'], bins=30, kde=True)
            plt.title('Price Distribution')
            plt.xlabel('Price (USD per barrel)')
            plt.ylabel('Frequency')
            plt.show()
            self.logger.info("Price distribution plot displayed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to plot price distribution: {e}")
            self._display_error_message("plot_price_distribution")

    def plot_yearly_average(self):
        """Plots average Brent Oil Prices per year."""
        try:
            df = self.data.copy().reset_index()
            df['Year'] = df['Date'].dt.year
            yearly_avg = df.groupby('Year')['Price'].mean().reset_index()
            
            plt.figure(figsize=(12, 6))
            sns.barplot(x='Year', y='Price', data=yearly_avg, hue='Year', legend=False, palette='viridis')
            plt.title('Average Yearly Brent Oil Prices')
            plt.xlabel('Year')
            plt.ylabel('Average Price (USD per barrel)')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.show()
            self.logger.info("Yearly average price plot displayed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to plot yearly average: {e}")
            self._display_error_message("plot_yearly_average")

    def plot_rolling_volatility(self, window=30):
        """Plots the rolling volatility (standard deviation) of Brent Oil Prices."""
        try:
            self.data['Rolling_Volatility'] = self.data['Price'].rolling(window=window).std()
            plt.figure(figsize=(10, 4))
            plt.plot(self.data.index, self.data['Rolling_Volatility'], color='orange', label=f'{window}-Day Rolling Volatility')
            plt.title(f'{window}-Day Rolling Volatility of Brent Oil Prices')
            plt.xlabel('Date')
            plt.ylabel('Volatility (Rolling Standard Deviation)')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            self.logger.info(f"{window}-day rolling volatility plot displayed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to plot rolling volatility: {e}")
            self._display_error_message("plot_rolling_volatility")
