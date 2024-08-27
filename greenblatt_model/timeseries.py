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
from util.all_stocks import all_stocks
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

test_stocks = ['SBUX','MO','META','AAPL','GOOG','AMZN','NFLX']#TODO a few stocks fail

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
resp = client.get_data_batch(companies=test_stocks, metrics=['roic', 'price_to_earnings','period_end_price'], period="FY-9:FY") # get 10 years eps growth, eps, pe ratio, and price for the test stocks
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

# S4: create stock time series objects for the test stocks

def create_stock_objects(tkr,minusyear):
    stock_name = "Test" #resp2.get('metadata', {}).get('name', "Unknown")
    ticker = tkr
    current_price = pd_stocks.loc[ticker, 'period_end_price'][minusyear]
    roic = pd_stocks.loc[ticker, 'roic'][minusyear]
    PE = pd_stocks.loc[ticker, 'price_to_earnings'][minusyear]
    if  (PE != 0) and (roic != 0):
        stock = Stock(stock_name, ticker, PE, roic, current_price,2024+minusyear) #TODO some stocks don't use 2023 as base year
        return stock
    stock = Stock("NULL", ticker, 1,1, current_price,2024+minusyear) 
    return stock #TODO this 'else' case breaks the system


def create_stock_TS_objects(ticker):
    #Create the list that is added to the TSStock object
    stockobjectlist = []
    for i in range(1,11):
        stockyear = create_stock_objects(ticker,-i)
        #print(stockyear)
        stockobjectlist.append(stockyear)
    return stockobjectlist


#Determine each stock's ranking for EY
def determine_rankings(stocks):
    sorted_stocks = sorted(stocks, key=lambda stock: stock.earnings_yield, reverse=True)
    for rank, stock in enumerate(sorted_stocks, start=1):
        stock.earnings_yield_rank = rank
    #Determine each stock's ranking for ROIC
    sorted_stocks = sorted(stocks, key=lambda stock: stock.ROIC, reverse=True)
    for rank, stock in enumerate(sorted_stocks, start=1):
        stock.ROIC_rank = rank
    for stock in stocks:
        stock.total_rank = stock.earnings_yield_rank + stock.ROIC_rank
    ranked_stocks = sorted(stocks, key=lambda stock: stock.total_rank)
    for i in range(len(ranked_stocks)):
        ranked_stocks[i].total_rank_relative = i
    return ranked_stocks

all_TS_stocks = [] # init a list of all Time series stocks
for i in range(len(test_stocks)):
    ticker = test_stocks[i]
    TSStock = TimeSeriesStock(ticker) # An object which contains a list of stock objects for the last 10 years
    TSStock.yearly_stock_objects = create_stock_TS_objects(ticker)
    if TSStock.yearly_stock_objects[-1].stock_name != 'NULL':
        all_TS_stocks.append(TSStock)
    else:
        print(f"Rejected stock: {TSStock.ticker}")
for yr in range (0,10):
    year_all_stocks = []
    for i in range(len(all_TS_stocks)):
        #print(all_TS_stocks[i])
        #print(all_TS_stocks[i].yearly_stock_objects[yr])
        year_all_stocks.append(all_TS_stocks[i].yearly_stock_objects[yr])
    determine_rankings(year_all_stocks)
for i in range(len(all_TS_stocks)):
    print(all_TS_stocks[i])

# S5: simulate buying and selling
print("Buying and selling simulation start")
for i in range(len(all_TS_stocks)):
    all_TS_stocks[i].buy_sell()
