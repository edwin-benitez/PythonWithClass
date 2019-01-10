import requests
import mysql.connector
import connectWithDB

f = open("apikey.txt", "r")
API_KEY = f.readline()
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=GE&apikey=' + API_KEY)
result = r.json()
monthly = result['Monthly Time Series']
month = input("Enter the end of month date to check stock (year-month-day): ")
avgMonth = monthly[month]

mydbl = connectWithDB.Mydba(input("Enter your host name: "), 
                            input("Enter your username: "), 
                            input("Enter your passowrd: "), 
                            input("Enter your database name: "))

mydb = mysql.connector.connect(
    host= mydbl.host,
    user= mydbl.user,
    password= mydbl.password,
    database= mydbl.database
)

mycursor = mydb.cursor()

sql = "INSERT INTO testTable (testMonth, testOpen, testHigh, testLow, testClose, testVolume) VALUES (%s, %s, %s, %s, %s, %s)"
val = (month, avgMonth['1. open'], avgMonth['2. high'], avgMonth['3. low'], avgMonth['4. close'], avgMonth['5. volume'])

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")