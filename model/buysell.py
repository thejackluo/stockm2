# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:00:53 2024

@author: atom2
"""

"""
DOCUMENTATION: input.py

Input: An array of stock objects
Output: An array of stock objects (w/ buy sell price)

STOCK Object (input):
    - stock_name
    - ticker
    - current_price
    - PE
    - EPS
    - EPS_growth
    - Years_with_positive_EPS
    - dampener

STOCK Object (output):
    - stock_name
    - ticker
    - current_price
    - PE
    - EPS
    - EPS_growth
    - Years_with_positive_EPS
    - buy_price
    - sell_price
    - projedted_interest_rate (givenc current price)
    - dampener
FUNCTION
Our goal is to go through an API and get all the data and produce

"""


import numpy as np
from eps import good_stocks


# A very basic module for evaluate stock, using the old evaluate functions on all good stocks
print("BUY SELL MODULE START")
print("=========================")
print("STOCKS RANKED BY PERCENT ABOVE/BELOW TARGET PRICE")
print("=========================")


def evaluate_all_stock():
    for stock in good_stocks:
        stock.evaluate()
        print("\n=========================")


def rank_by_percent_above_below(stocks): # Returns a list of stocks object sorted by percent above or below the buy price
    return sorted(stocks, key=lambda x: x.get_current_price_above_below_buy_price_percent(), reverse=False)
good_stocks = rank_by_percent_above_below(good_stocks)
evaluate_all_stock()



# Original small model

#if __name__ == "__main__":
    # Input is a list of Earnings per Share (EPS) and Price to Earnings (PE) ratios (test stocks)
    #TPLEPS = [0.31, 0.4730, -0.1330, 1.3400, 1.1750, 0.5260, -0.4480, 0.5340, 0.6590, -0.0870]
    #TPLPE = [28.25, 21.24, 55.65, 35.93, 20.04, 19.01, 32.03, 35.88, 40.42, 29.73]

    # Input the stock's name, ticker, EPS for 2023, EPS growth, PE, and current price
    #tpl = Stock("Texas Pacific Land", "TPL", 52.77, TPLEPS, TPLPE, 1650)
    #tpl.evaluate()
