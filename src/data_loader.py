"""
# src/data_loader.py
# This module fetches, preprocesses, and saves stock data from Yahoo Finance.
# It includes functions to get data, preprocess it, and save it to a CSV file.
# Author: Kenneth LeGare
# Version: 1.0
# Dependencies: pandas, yfinance
"""

import pandas as pd 
import yfinance as yf

def get_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    
    Parameters:
    ticker (str): Stock ticker symbol.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: DataFrame containing historical stock prices.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def preprocess_data(data):
    """
    Preprocess the stock data.
    
    Parameters:
    data (pd.DataFrame): Raw stock data.
    
    Returns:
    pd.DataFrame: Preprocessed stock data with necessary columns.
    """
    # Ensure the DataFrame has a DateTime index
    data.index = pd.to_datetime(data.index)
    
    # Select relevant columns
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    
    # Fill missing values
    data.fillna(method='ffill', inplace=True)
    
    return data

def save_data(data, filename):
    """
    Save the preprocessed data to a CSV file.
    
    Parameters:
    data (pd.DataFrame): Preprocessed stock data.
    filename (str): Name of the file to save the data.
    """
    data.to_csv(filename, index=True)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Example usage
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    
    raw_data = get_data(ticker, start_date, end_date)
    preprocessed_data = preprocess_data(raw_data)
    save_data(preprocessed_data, f"{ticker}_data.csv")
