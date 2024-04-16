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
import os

# S0: Input

# S1: API Key and set up
load_dotenv()  # take environment variables from .env.

api_key = os.getenv('QUICKFS_API_KEY')

if api_key:
    print("API Key:", api_key)
else:
    print("Environment variable not found.")

# S2: Get data from API
