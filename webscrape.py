import json
import requests
import sqlite3

stock_price_url = 'https://financialmodelingprep.com/api/company/price/'
income_statement_url = "https://financialmodelingprep.com/api/financials/income-statement/"
balance_sheet_url = "https://financialmodelingprep.com/api/financials/balance-sheet-statement/"
cash_flow_url = "https://financialmodelingprep.com/api/financials/cash-flow-statement/"
profile_url = "https://financialmodelingprep.com/api/company/profile/"

Ticker = input("Which company ticker would you like to analyze? ")
Ticker = Ticker.upper()


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


print(get_price(Ticker))
print(get_income_statement(Ticker)["Revenue"]["2014-09"])
print(get_balance_sheet(Ticker)["Total cash"]["2014-09"])
print(get_cash_flow(Ticker)["Net income"]["2014-09"])

# data = response.read().decode()
# nmap = json.loads(data)

# url = urllib.request.urlopen(stock_price_url)
# data = json.loads(url.read().decode())

# print(data)
