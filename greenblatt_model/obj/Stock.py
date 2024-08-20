"""
Stock object class for Joel Greenblatt's method AKA the MAGIC FORMULA

TODO: write documentations for each method
"""
import numpy as np

class Stock:

    # Attributes
    def __init__(self, stock_name, ticker, PE, ROIC, current_price,year):
        self.stock_name = stock_name
        self.ticker = ticker
        self.PE = PE
        self.earnings_yield = 1/PE # the inverse of PE
        self.ROIC = ROIC
        self.current_price = current_price
        self.earnings_yield_rank = -1
        self.ROIC_rank = -1
        self.total_rank = -1
        self.total_rank_relative = -1
        self.year = year
    # General Util
    def __str__(self):
        # please print the entire stock object
        return f"Stock: {self.stock_name} ({self.ticker,self.year}) \n" + \
            f"Earnings Yield: {self.earnings_yield}, rank of {self.earnings_yield_rank}\n" + \
            f"Return on Invested Capital: {self.ROIC}, rank of {self.ROIC_rank}\n" + \
            f"Total Rank: {self.total_rank}, relative {self.total_rank_relative}\n" + \
            f"Current Price: {self.current_price}\n"
    