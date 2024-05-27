# stock-model-2

stock model v2 for qunatamental analysis and beyond

# project structure

## test

- chatgpt_metrics.txt: a file to process quickfs metrics for chatGPT to write API calls
- input_test_v1: terminal output for first iteration of the model objects
- quickfs_api_template.txt: json template for quickfs API calls

## iter 1: quickfs

pipeline: input.py -> eps.py -> buysell.py
all_stocks.py: a list of stock tickers

- input.py: takes in a ticker and returns the EPS data
- eps.py: takes in the EPS data and returns the EPS growth rate
- buysell.py: takes in the EPS growth rate and returns a buy/sell recommendation

## iter 2: alphavantage

- avinput.py: **********\_\_\_**********
- alplhavantagemethods.py: **********\_\_**********

## backtesting

- backtesting.py: **********\_\_\_**********

# references

notion wiki
