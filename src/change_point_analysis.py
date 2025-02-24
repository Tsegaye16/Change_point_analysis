import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ruptures as rpt
import pymc as pm
import arviz as az
from datetime import timedelta
from scipy import stats

class ChangePointAnalyzer:
    """
    A class for analyzing event-specific changes in Brent oil prices, including CUSUM and Bayesian 
    change point detection, as well as statistical analysis of price changes around events.
    
    Parameters:
    - price_data (pd.DataFrame): DataFrame with 'Date' as index and 'Price' column.
    - logger (logging.Logger): Logger instance for logging messages, warnings, and errors.
    """
    
    def __init__(self, price_data, logger=None):
        self.price_data = price_data
        self.logger = logger
        self.mean_price = self.price_data['Price'].mean()
        
        
    def calculate_cusum(self):
        """Calculates and plots the CUSUM of deviations from the mean price."""
        try:
            cusum = (self.price_data['Price'] - self.mean_price).cumsum()
            plt.plot(self.price_data.index, cusum, label='CUSUM of Price Deviations', color='orange')
            plt.title('CUSUM Line Plot of Brent Oil Price Deviations')
            plt.xlabel('Date')
            plt.ylabel('Cumulative Sum of Deviations (USD)')
            plt.legend()
            plt.grid()
            plt.show()
            self.logger.info("CUSUM plot created successfully.")
        except Exception as e:
            self.logger.error("Error calculating or plotting CUSUM: %s", e)
    
    def detect_change_point(self):
        """Detects change points using the CUSUM-based method from the ruptures package."""
        try:
            
            # Extract the price series for change point detection
            price_df = self.price_data.reset_index()
            price_series = price_df['Price'].values

            # Apply the CUSUM-based method for change point detection
            algo = rpt.Binseg(model="rbf").fit(price_series)
            change_points = algo.predict(n_bkps=5)  # Adjust n_bkps for more or fewer breakpoints

            # Extract and print the year of each change point
            change_years = [price_df['Date'].iloc[cp] for cp in change_points[:-1]]  # Exclude the last index (end of data)
            print("Detected change point years:", change_years)

            # Plotting the Brent Oil Price with change points
            plt.plot(price_df['Date'], price_df['Price'], label='Brent Oil Price', color='blue')

            # Overlay detected change points with year annotations
            for cp in change_points[:-1]:  # Exclude the last point (end of data)
                year = price_df['Date'].iloc[cp].year
                plt.axvline(price_df['Date'].iloc[cp], color='red', linestyle='--')
                plt.text(price_df['Date'].iloc[cp], price_df['Price'].iloc[cp], str(year), color="red", fontsize=10)

            # Enhancements
            plt.title('Brent Oil Prices with CUSUM Change Points and Years')
            plt.xlabel('Date')
            plt.ylabel('Price (USD)')
            plt.legend()
            plt.grid()
            plt.show()
          
        except Exception as e:
            self.logger.error("Error detecting change points: %s", e)
            
            
    def bayesian_change_point_detection(self):
        """Performs Bayesian change point analysis using PyMC."""
        try:
            data = self.price_data['Price'].values
            prior_mu = np.mean(data)
            
            with pm.Model() as model:
                change_point = pm.DiscreteUniform('change_point', lower=0, upper=len(data) - 1)
                mu1 = pm.Normal('mu1', mu=prior_mu, sigma=5)
                mu2 = pm.Normal('mu2', mu=prior_mu, sigma=5)
                sigma1 = pm.HalfNormal('sigma1', sigma=5)
                sigma2 = pm.HalfNormal('sigma2', sigma=5)
                
                likelihood = pm.Normal(
                    'likelihood',
                    mu=pm.math.switch(change_point >= np.arange(len(data)), mu1, mu2),
                    sigma=pm.math.switch(change_point >= np.arange(len(data)), sigma1, sigma2),
                    observed=data
                )
                
                trace = pm.sample(4000, tune=2000, chains=4, random_seed=42)
                self.logger.info("Bayesian sampling completed successfully.")
                
                az.plot_trace(trace)
                plt.show()
                
                s_posterior = trace.posterior['change_point'].values.flatten()
                change_point_estimate = int(np.median(s_posterior))
                change_point_date = self.price_data.index[change_point_estimate]
                
                print(f"Estimated Change Point Date: {change_point_date}")
                self.logger.info("Estimated change point date: %s", change_point_date)
                
                return change_point_date
        except Exception as e:
            self.logger.error("Error in Bayesian change point analysis: %s", e)
    

   