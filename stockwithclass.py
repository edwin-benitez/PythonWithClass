import mysql.connector
import stockapi

class Mydba:

    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

mydbl = Mydba(input("Enter your host name: "), 
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
val = (stockapi.month, stockapi.stockMonth.open, stockapi.stockMonth.high, stockapi.stockMonth.low, 
       stockapi.stockMonth.close, stockapi.stockMonth.volume)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")