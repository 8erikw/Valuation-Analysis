import json
import requests
import sqlite3
import bs4
import lxml

sqlite_file = "myaddddddddd_hdb.sqlite"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

stock_price_url = 'https://financialmodelingprep.com/api/company/price/'
income_statement_url = "https://financialmodelingprep.com/api/financials/income-statement/"
balance_sheet_url = "https://financialmodelingprep.com/api/financials/balance-sheet-statement/"
cash_flow_url = "https://financialmodelingprep.com/api/financials/cash-flow-statement/"
profile_url = "https://financialmodelingprep.com/api/company/profile/"
ticker_url = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

soup = bs4.BeautifulSoup(ticker_url.text, "lxml")
tickers = soup.select("td:nth-child(2) .text")
ticker_list = [title.text for title in tickers]

print(ticker_list)



# Ticker = input("Which company ticker would you like to analyze? ")
# Ticker = Ticker.upper()




def get_price(ticker):
    price_url = stock_price_url + ticker
    response = requests.get(price_url).text
    response = response[5:-5]
    result = json.loads(response)
    return result[ticker]['price']


def get_income_statement(ticker):
    income_url = income_statement_url + ticker
    response = requests.get(income_url).text
    response = response[5:-5]
    result = json.loads(response)[ticker]
    # What is needed in an income statement?
    return result

def get_cash_flow(ticker):
    cash_url = cash_flow_url + ticker
    response = requests.get(cash_url).text
    response = response[5:-5]
    result = json.loads(response)[ticker]
    # What is needed in a cash flow?
    return result


def get_balance_sheet(ticker):
    balance_url = balance_sheet_url + ticker
    response = requests.get(balance_url).text
    response = response[5:-5]
    result = json.loads(response)[ticker]
    # What is needed in a balance sheet?
    return result


lineItemMap = {}
index = 0
for ticker in ticker_list:
    income_statement_by_ticker = get_income_statement(ticker)
    for key1 in income_statement_by_ticker.keys():
        if key1 not in lineItemMap.keys():
            lineItemMap[key1] = index
            index+=1
            print(lineItemMap)






# listOfData = []

# for ticker in ticker_list:
#     tickerData = []
#     income_statement_by_ticker = get_income_statement(ticker)
#     for key1 in income_statement_by_ticker.keys():
#         tickerData.append(key1)
#     #     c.execute("INSERT INTO {ticker} ({lineItem}) VALUES (?)".\
#     #               format(ticker=ticker, lineItem="LineItem"), (key1,))
#         # for key2 in income_statement_by_ticker[key1].keys():
#         #     #print(ticker, key1, key2, income_statement_by_ticker[key1][key2])
#         #     c.execute("INSERT INTO {ticker} ({y1}) VALUES ({value})".\
#         #               format(ticker=ticker, y1=key2[:4], value=income_statement_by_ticker[key1][key2]))
#
#     listOfData.append(tickerData)











#
# print(get_price(Ticker))
# print(get_income_statement(Ticker)["Revenue"]["2014-09"])
# print(get_balance_sheet(Ticker)["Total cash"]["2014-09"])
# print(get_cash_flow(Ticker)["Net income"]["2014-09"])



# data = response.read().decode()
# nmap = json.loads(data)

# url = urllib.request.urlopen(stock_price_url)
# data = json.loads(url.read().decode())

# print(data)
