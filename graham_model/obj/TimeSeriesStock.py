"""
Stock object time series for Ben graham's method

TODO: write documentations for each method
"""
import numpy as np

class TimeSeriesStock:
    # Attributes
    def __init__(self, ticker):
        self.stock_name = "TEST"
        self.ticker = ticker
        self.yearly_stock_objects = []

    # General Util
    def __str__(self):
        # Print the entire stock object
        s = f"========================================\nTIME SERIES FOR: {self.stock_name} ({self.ticker})\nSTOCK OBJECTS:\n========================================\n"
        for stock in self.yearly_stock_objects:
            s += str(stock) + "\n"
        return s

    def buy_sell(self):
        if len(self.yearly_stock_objects) != 10:
            print(f"Module does not support not 10 years of history stocks! {self.ticker}")
            return
        total_amount_invested = 0 
        fixed_profit = 0
        buy_year = 0
        buy_price = 0
        current_price = 0
        current_year = 0
        
        for stock in reversed(self.yearly_stock_objects):
            current_price = stock.current_price
            current_year = stock.year
            if total_amount_invested == 0 and stock.current_price_above_nav < 0 and stock.current_price_above_nav > -1:  # Check if it's a good buy - this ratio is probably a bit strict as the book is 20 yrs old but we see
                print(f"Buying {stock.ticker} on {stock.year} at {stock.current_price}")
                total_amount_invested += stock.current_price #TODO Standardise every purchase to $1000
                buy_year = stock.year
                buy_price = stock.current_price
            elif total_amount_invested > 0 and stock.current_price_above_nav > 2:  # Check if it's a good sell
                print(f"Selling {stock.ticker} on {stock.year} at {stock.current_price}")
                profit = (stock.current_price - (total_amount_invested)) 
                print(f"Profit: {profit} Buy: {buy_price} Sell: {stock.current_price}, Annualised Return: {((stock.current_price/buy_price)**(1/(stock.year-buy_year)))}")
                total_amount_invested = 0
                buy_year = 0
                buy_price = 0
                fixed_profit += profit

        if fixed_profit == 0 and total_amount_invested == 0:
            print(f"No Purchases Made for stock {self.yearly_stock_objects[0].ticker}")
        print(f"Final Profit: {fixed_profit}")
        if total_amount_invested > 0:
            print(f"Current holdings {current_price} from original buy at: {total_amount_invested}")
            print(f"Annual return on current holdings: {((current_price/buy_price)**(1/(current_year-buy_year)))}")