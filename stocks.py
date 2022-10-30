import requests
from bs4 import BeautifulSoup
import sys

def getStock(symbol):

    print("Symbol coming in: ")
    print(symbol)
    print(" ")
    
    #URL that is used to get stock data using the stock symbol
    URL = f'https://money.cnn.com/quote/forecast/forecast.html?symb={symbol}'.format(symbol)
    print("URL used to scrape data from is: ")
    print(URL)
    print(" ")

    page = requests.get(URL)

    # Using BeautifulSoup to scrape data
    soup = BeautifulSoup(page.content, 'html.parser')

    # Empty list to store stock data in
    stockData = ""

    # Save forecast and anaylyst data 
    for line in soup.find_all(class_='wsod_twoCol clearfix'):
        stockData += line.text

    # Remove unnecessary characters at the end of the data
    stockData = stockData[:-50]

    # Save to text file
    stock_f = open('stock.txt', 'r+', encoding="utf-8")
    stock_f.truncate()
    stock_f.write(stockData)

if __name__ == '__main__':
    # Stock Symbol user entered
    stock = sys.argv[1]
    # Call web scraper function using variable passed from subprocess.run()
    getStock(stock)













