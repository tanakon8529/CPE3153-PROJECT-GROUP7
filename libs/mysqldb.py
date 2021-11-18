import mysql.connector

db = mysql.connector.connect(
    host="3.1.221.178",
    database='training',
    user="root",
    password="4321"
    )

cursor = db.cursor()

sql = "SELECT tweet FROM tweet"
cursor.execute(sql)
results = cursor.fetchall()

tweet = list(results[0])
print(tweet)

db.close()