"""
This module implements various performance metrics for evaluating trading strategies.
It includes functions for calculating common metrics such as Sharpe ratio, maximum drawdown, and others.
Author: Kenneth LeGare
Version: 1.0
Dependencies: pandas, numpy, backtester
"""
import pandas as pd
import numpy as np
from backtester import backtest 

def calculate_sharpe_ratio(returns, risk_free_rate=0.01):
    """
    Calculate the Sharpe ratio of a series of returns.
    
    Parameters:
    returns (pd.Series): Series of returns.
    risk_free_rate (float): Risk-free rate, default is 0.01.
    
    Returns:
    float: Sharpe ratio.
    """
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std()

def calculate_max_drawdown(returns):
    """
    Calculate the maximum drawdown of a series of returns.
    Parameters:
    returns (pd.Series): Series of returns.
    Returns:
    float: Maximum drawdown.
    """
    cumulative_returns = (1 + returns).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min()

