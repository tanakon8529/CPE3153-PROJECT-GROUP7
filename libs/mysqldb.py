import mysql.connector

mydb = mysql.connector.connect(
  host="3.1.221.178",
  user="root",
  password="4321"
)

print(mydb)