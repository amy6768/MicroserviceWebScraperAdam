Communication Contract
A. How to request data - In order to receive the scraped data for the "Stock Price Forecast" and 
"Analysts Recommendations",  you will need to use the subprocess.run call:

stock_subprocess = subprocess.run(["python3", "stocks.py", stock])

The stocks.py file takes in the variable 'stock' from the subprocess.run and uses it to create
a URL for the requested stock. The data is then scraped from the URL and stored as a string. The
string is then saved into a .txt file.

B. How to receive data - You will receive the data in a .txt file named stock.txt that can be 
used to display the information on your app.

C. UML Sequence Diagram - 

 ------------------         --------------           ----------               ----------
        App                  callStocks.py            stocks.py                   URL   
 ------------------         --------------           ----------               ----------
         |                        |                       |                        |
    [User selects a
    stock from ----------->       |                       |                        |
    a drop-down   
    menu]                    [Subprocess call             |                        |
        |   |                    to stocks.py] ------->    
        |   |                    |   |                    |                        |
        |   |                    |   |               [Web Scraper is                  
        |   |                    |   |               used to get                 |   |  
        |   |                    |   |               analysis and ------>        |   | 
        |   |                    |   |               forecast data for           |   |  
        |   |                    |   |               stock]                      |   | 
        |   |                    |   |                  |   |                    |   |
        |   |                    |   |                  |   |   <-------- [Returns scraped data]
        |   |                    |   |                  |   |                      X
        |   |                    |   |                  |   | 
        |   |                    |   | <------------ [Returns a .txt 
        |   |                    |   |               file]
        |   |                    |   |                    X
        |   |                    |   |
        |   |      <--------- [.txt file is saved]
    [.txt file is diplayed      in app]
    on app screen]                  X
          X