"""
src/backtester.py
This module implements a backtesting framework using Backtrader.
It includes a simple strategy that uses two moving averages to generate buy/sell signals.
Author: Kenneth LeGare
Version: 1.0
Dependencies: pandas, yfinance, backtrader, dataclasses
"""
from dataclasses import dataclass
import pandas as pd
import yfinance as yf
import backtrader as bt

class backtest(bt.Strategy):
    """
    A simple backtesting strategy using Backtrader.
    This strategy uses two simple moving averages (SMA) to generate buy/sell signals.
    It buys when the short SMA crosses above the long SMA and sells when it crosses below.
    """
    params = {
        'sma_short': 10,  # Short moving average period
        'sma_long': 30    # Long moving average period
    }

    price_data: pd.DataFrame
    period: int
    name: str

    def __init__(self):
        self.sma_short = bt.ind.SMA(period=self.params.sma_short)
        self.sma_long = bt.ind.SMA(period=self.params.sma_long)

    def signal_strategy(self, price_data, period, name):
        # Calculate SMA
        sma = price_data.rolling(period).mean()
        # Define the signal-based Strategy
        bt_strategy = bt.Strategy(name, 
                              [bt.algos.SelectWhere(price_data > sma),
                               bt.algos.WeighEqually(),
                               bt.algos.Rebalance()])
        # Return the backtest
        return bt.Backtest(bt_strategy, price_data)

    def buy_and_hold(price_data, name):
        # Define the benchmark strategy
        bt_strategy = bt.Strategy(name, 
                              [bt.algos.RunOnce(),
                               bt.algos.SelectAll(),
                               bt.algos.WeighEqually(),
                               bt.algos.Rebalance()])
        # Return the backtest
        return bt.Backtest(bt_strategy, price_data)

    def run_backtest(self, data, name):
        """
        Run the backtest with the provided data.
        
        Parameters:
        data (pd.DataFrame): DataFrame containing historical stock prices.
        
        Returns:
        bt.Backtest: Backtest object containing the results.
        """
        self.price_data = data
        self.period = len(data)
        self.name = 'SMA Strategy'
        
        # Create a Backtrader Cerebro engine
        cerebro = bt.Cerebro()
        
        # Add the strategy to Cerebro
        cerebro.addstrategy(self.signal_strategy, price_data=self.price_data, period=self.period, name=self.name)
        
        return cerebro.run()
