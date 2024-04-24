"""
DOCUMENTATION: input.py

Input: An array of ALL tickers we want to test
Output: An array of stock objects 

STOCK Object:
    - ticker
    - stock_name
    - EPS_2023
    - EPS_growth (list of 10 year EPS growth)
    (other data for the future)

FUNCTION
Our goal is to go through an API and get all the data and produce
"""

from dotenv import load_dotenv
from quickfs import QuickFS
from all_stocks import all_stocks
from obj.stock import Stock
import os
import json
import pandas as pd

# S0: Input (US indexes Russel 1000 + 2000 V2) (S&P 500 V1)

# create a list of the three test stocks (1, 5, 12) ticker only no object
print("INPUT TEST REPORT") # print the first 3 stock in the all stock list as testing purposes
# test_stocks = [all_stocks[1], all_stocks[5], all_stocks[12]]

# please list out the first 300 stocks for testing purposes
test_stocks = all_stocks[:10]
print("S0:", test_stocks) # AAPL, GOOGL, TSLA 

# TODO: write a check for stocks whether they are in the US avaialble stocks (for backtesting purposes)

# S1: API Key and set up
load_dotenv(override=True)  # take environment variables from .env.

api_key = os.getenv('QUICKFS_API_KEY')

if api_key:
    print("S1: API Key Success")
    print(api_key)
else:
    print("ERROR S1: Environment variable not found.")

client = QuickFS(api_key)
print("S1: Client Success, current usage:", client.get_usage())

# S2: For stock 1, 5, and 12 based on indice, import the stock object (attributes above) and initialize some data points based on the output using API calls, then print out the stock object for testing (all 3)

# EPS Module

# get 10 years eps growth, eps, pe ratio, and price for the test stocks
resp = client.get_data_batch(companies=test_stocks, metrics=['eps_diluted_growth', 'price_to_earnings'], period="FY-9:FY") # Example Function

# Check the status of the call
print("S2: client resp:", client.resp) # If it says 207, you have content to use.
print("S2: client content:", client.resp._content) # check the error

# S3: convert into PANDAS dataframe for easier manipulation
pd_stocks = json.loads(client.resp._content.decode('utf-8'))['data'] # filter and extract for the companies that you have data
pd_stocks = pd.DataFrame(pd_stocks) # transform it to a pandas dataframe (if you want it)
print("S3: organized stocks", pd_stocks)

# S4: create stock objects for the test stocks
# using numpy, get the average EPS growth for each stock, and create the stock object for each stock
# get the most recent eps growth based on teh last eps diluted growth for each stock for inputting into the stock object later\

# please ignore stock name, and also current prices for now (set name to TEST, and set current price to -1)

# create a list of stock objects
all_stocks = []

for i in range(len(test_stocks)):
    stock_name = "TEST" #TODO
    ticker = test_stocks[i]
    EPS_2023 = 0 #TODO
    EPS_growth = pd_stocks.loc[ticker, 'eps_diluted_growth']
    PE = pd_stocks.loc[ticker, 'price_to_earnings']
    current_price = -1 #TODO

    stock = Stock(stock_name, ticker, EPS_2023, EPS_growth, PE, current_price)
    all_stocks.append(stock)


# print the stock objects
print("S4: Stock Objects")
for stock in all_stocks:
    print(stock)


# S5: Output the stock objects for the next module


# ARCHIVES
# Stock 1: AAPL
# AAPL = client.get_data_full(symbol='AAPL:US') 
# print(AAPL)

# client.get_data_batch(companies=test_stocks, metrics=['eps', 'roic'], period="FY-2:FY") # Example Function





