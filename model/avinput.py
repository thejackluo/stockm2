"""
DOCUMENTATION: avinput.py

INPUT: An array of ALL tickers we want to test
OUTPUT: An array of stock objects 

STOCK OBJ:
    - ticker
    - stock_name
    - EPS_2023
    - EPS_growth (list of 10 year EPS growth)
    (other data for the future)

FUNCTION
Our goal is to go through an API and get all the data and produce ______________

This file uses Alpha Vantage API
"""

from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import requests
from all_stocks import all_stocks
from obj.Stock import Stock
import os
import json
import pandas as pd


# S0: Get input (US indexes Russel 1000 + 2000 V2) (S&P 500 V1)
"""
# create a list of the three test stocks (1, 5, 12) ticker only no object
# test_stocks = [all_stocks[1], all_stocks[5], all_stocks[12]] # print the first 3 stock in the all stock list as testing purposes # AAPL, GOOGL, TSLA????
"""
'''
print("=====================================")
print("P0: Input Module")
print("=====================================") 
'''

# S1: Add API KEY and Set Up AV SDK
load_dotenv(override=True)  # take environment variables from .env.
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
if api_key:
    print("S0: API Key Success:", api_key)
    client = api_key
    #print("S0: AV SDK Client Success, current usage:", client.queries()) #TODO
else:
    print("ERROR S0: Environment or API_Key variable not found.")
test_stocks = all_stocks

print("S1: Print all the data for a Sample Stock (SSD)")
ts = TimeSeries(key = api_key,output_format = 'pandas')
fd = FundamentalData(key = api_key,output_format = 'pandas')

sample_FD = fd.get_balance_sheet_annual('SSD') # there appears to be functions which grab Balance Sheet, Cashflow statement, and income statement, but earnings cannot find?
print(sample_FD)
print('List of Goodwill for stock SSD is', sample_FD[0]['goodwill']) #
print('sample test: the number 502550000 is SSD goodwill in 2023. It should match the toprightmost number')

'''
my_string = str(sample_FD)
my_string = my_string.split()
print(my_string)

#ignore below this

#resp = client.get_data_batch(companies=test_stocks, metrics=['eps_diluted_growth', 'price_to_earnings','eps_diluted','period_end_price'], period="FY-9:FY") # get 10 years eps growth, eps, pe ratio, and price for the test stocks
# Check the status of the call

all_stocks = [] # initalize a list of stock objects

for i in range(len(test_stocks)):
    resp2 = client.get_data_full(symbol=test_stocks[i]) #TODO this takes decent amount of time
    stock_name = resp2.get('metadata', {}).get('name', "Unknown")
    ticker = test_stocks[i]
    current_price = pd_stocks.loc[ticker, 'period_end_price'][-1]# alpha_vantage_current_price_obtainer(ticker)

    EPS_2023 = pd_stocks.loc[ticker, 'eps_diluted'][-1]
    EPS_growth = pd_stocks.loc[ticker, 'eps_diluted_growth']
    PE = pd_stocks.loc[ticker, 'price_to_earnings']

    stock = Stock(stock_name, ticker, EPS_2023, EPS_growth, PE, current_price)

    
    all_stocks.append(stock)


print("S4: Stock Objects:") # Print the final stock objects based on the stringto method from all stocks
for stock in all_stocks:
    print(stock)
'''