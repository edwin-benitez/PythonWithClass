import requests

f = open("apikey.txt", "r")
API_KEY = f.readline()
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=GE&apikey=' + API_KEY)
result = r.json()
monthly = result['Monthly Time Series']
month = input("Enter the end of month date to check stock (year-month-day): ")
avgMonth = monthly[month]
class MyApiMonth:
    def __init__(self, open, high, low, close, volume):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

#This will get the open, high, low, and close price along with the volume
stockMonth = MyApiMonth(avgMonth['1. open'], avgMonth['2. high'], avgMonth['3. low'], avgMonth['4. close'],
                        avgMonth['5. volume'])