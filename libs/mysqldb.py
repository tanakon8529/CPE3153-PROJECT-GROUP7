
from libs.setting import MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD
import mysql.connector


def mysql_connect(sql):
    db = mysql.connector.connect(
            host = MYSQL_HOST,
            database = MYSQL_DATABASE,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
        )

    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

