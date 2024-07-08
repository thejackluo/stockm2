"""
DOCUMENTATION: timeseries.py

INPUT: An array of ALL tickers we want to test
OUTPUT: An array of Time series stock objects - 
each one contains a 10-year array of the stock objects for the stock so we can do backtesting


FUNCTION
Our goal is to go through an API and get all the data and produce ______________

This file uses QUICKFS as the API of choice


LIMITATIONS:
Period end price data is only available to the period end price (end of 2023), can be optimized to end of quarter price, but still not ideal
Certain stocks break the model
current price is taken from 1/1/2024 while the rest of the data is from 2023- this is not ideal as I don't why it does that but its intended for backtesting - We can't make decisions retroactively
This model alone cannot screen for shitty stocks - when NAV is negative#
"""

from dotenv import load_dotenv
from quickfs import QuickFS
# from util.all_stocks import all_stocks
from obj.TimeSeriesStock import TimeSeriesStock
from obj.Stock import Stock
import os
import json
import pandas as pd
#from input import create_stock_objects

# S0: Get input (US indexes Russel 1000 + 2000 V2) (S&P 500 V1)

print("=====================================")
print("P0: Time series creation base Module")
print("=====================================") 

test_stocks = ["LULU"]
#TODO a few stocks fail
# Works: META, GOOG, TPL, VSAT, YUM, ODFL, XOM, MSFT, GHC, JEF, GMAB, LULU
# Fails: WEN, YMM, MBLY, TUYA, HUYA
print("S0: Stock List:", test_stocks) 


# S1: Add API KEY and Set Up QuickFS SDK
load_dotenv(override=True)  # take environment variables from .env.
api_key = os.getenv('QUICKFS_API_KEY')

if api_key:
    print("S1: API Key Success:", api_key)
    client = QuickFS(api_key)
    print("S1: QuickFS SDK Client Success, current usage:", client.get_usage())
else:
    print("ERROR S1: Environment or API_Key variable not found.")



# S2: For test_stocks list, RETRIEVE different attributes of the stock based on the API and initialize new stock object
# EPS Module Data V1
resp = client.get_data_batch(companies=test_stocks, metrics=['total_current_assets', 'total_current_liabilities','period_end_price','market_cap','shares_diluted','lt_debt'], period="FY-9:FY") # get 10 years eps growth, eps, pe ratio, and price for the test stocks
# Check the status of the call
#print("S2: client resp number:", client.resp) # Outputs response number. If it says 207, you have content to use.
#print("S2: client content:", client.resp._content) # Outputs the content of the response, if there is an error, check the error


# # # EPS Module Data V2: use the client.get_data_full to get metadata for stock and use a for loop to run through all_stocks ticker, then in each iteration, print out the data
# for ticker in test_stocks:
#     print("S2: ticker: ===================================", ticker)
#     print(client.get_data_full(symbol=ticker))



# S3: Convert json data into into PANDAS dataframe for easier manipulation
pd_stocks = json.loads(client.resp._content.decode('utf-8'))['data'] # filter and extract for the companies that you have data
pd_stocks = pd.DataFrame(pd_stocks) # transform it to a pandas dataframe
#print("S3: test_stocks Pandas DataFrame", pd_stocks) # Output the dataframe to VISUALIZE the data

# S4: create stock objects for the test stocks

def create_stock_objects(tkr,minusyear):
    stock_name = "Test" #resp2.get('metadata', {}).get('name', "Unknown")
    ticker = tkr
    current_price = pd_stocks.loc[ticker, 'period_end_price'][minusyear]# alpha_vantage_current_price_obtainer(ticker)
    total_current_assets = pd_stocks.loc[ticker, 'total_current_assets'][minusyear]
    liabilities = pd_stocks.loc[ticker, 'total_current_liabilities'][minusyear]
    market_cap = pd_stocks.loc[ticker, 'market_cap'][minusyear]
    shares = pd_stocks.loc[ticker, 'shares_diluted'][minusyear]
    lt_debt = pd_stocks.loc[ticker, 'lt_debt'][minusyear]
    
    # Check if total_current_assets is an integer - Certain stocks,
    # most notably banks and insurance I think do not
    # work properly for the assets-liabilities method
    if isinstance(total_current_assets, int) and isinstance(liabilities, int) and isinstance(shares, int) and shares != 0:
        stock = Stock(stock_name, ticker, total_current_assets, liabilities, market_cap, shares, lt_debt, current_price,2024+minusyear) #TODO some stocks don't use 2023 as base year
        return stock
    print("Error: ", ticker)
    return


def create_stock_TS_objects(ticker):
    #Create the list that is added to the TSStock object
    stockobjectlist = []
    for i in range(1,11):
        stockyear = create_stock_objects(ticker,-i)

        stockobjectlist.append(stockyear)
    return stockobjectlist

all_stocks = [] # initalize a list of stock objects
print("NOTE: current price is taken from 1/1/2024 while the rest of the data is from 2023- this is not ideal as I don't why it does that but its intended for backtesting - We can't make decisions retroactively")
for i in range(len(test_stocks)):
    
    ticker = test_stocks[i]
    TSStock = TimeSeriesStock(ticker) # An object which contains a list of stock objects for the last 10 years
    TSStock.yearly_stock_objects = create_stock_TS_objects(ticker)
    print(TSStock)

'''

print("S4: Stock Objects:") # Print the final stock objects based on the stringto method from all stocks
for stock in all_stocks:
    print(stock)
'''

# S5: See eps.py


# ARCHIVES
"""
# Stock 1: AAPL
# AAPL = client.get_data_full(symbol='AAPL:US') 
# print(AAPL)

# client.get_data_batch(companies=test_stocks, metrics=['eps', 'roic'], period="FY-2:FY") # Example Function

# Old Current Price Retrieval
# current_price = pd_stocks.loc[ticker, 'period_end_price'][-1] #TODO - uses period end prices (believe it is year end), not the current price

"""




