import subprocess
import sys


stock = input("What stock analysis would you like to see? Enter stock symbol:  ")
# BEST, GOOG, WB, AMZN (sample stocks)

# Call the subprocess to get stock data
stock_subprocess = subprocess.run(["python3", "stocks.py", stock])

# Check content of stock.txt file for stock information
f = open("stock.txt","r")
print("Content of text file is: ") 
print(f.readlines())
print()
f.close()


