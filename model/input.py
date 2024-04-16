"""
DOCUMENTATION: input.py

Input: An array of ALL tickers we want to test
Output: An array of stock objects 

STOCK Object:
    - stock_name
    - ticker
    - current_price
    - PE
    - EPS
    - EPS_growth

FUNCTION
Our goal is to go through an API and get all the data and produce
"""

from dotenv import load_dotenv
from quickfs import QuickFS
from all_stocks import all_stocks
import os

# S0: Input (US indexes Russel 1000 + 2000 V2) (S&P 500 V1)

# print the first 3 stock in the all stock list as testing purposes
print("INPUT TEST REPORT")
print("S0:", all_stocks[0], all_stocks[1], all_stocks[2])

# S1: API Key and set up
load_dotenv()  # take environment variables from .env.

api_key = os.getenv('QUICKFS_API_KEY')

if api_key:
    print("S1: API Key Success")
else:
    print("S1: Environment variable not found.")

client = QuickFS(api_key)
print("S1: Client Success, current usage:", client.get_usage())

# S2: Get data from API



