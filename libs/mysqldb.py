
from libs.setting import MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD
import mysql.connector
import redis
import re
import pickle


def mysql_connect():
    db = mysql.connector.connect(
            host = MYSQL_HOST,
            database = MYSQL_DATABASE,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
        )

    # sql = f''' SELECT tweet FROM tweet WHERE tweet Like '%{search}%' '''
    sql = f''' SELECT tweet FROM tweet '''
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def search_database(search):
    res = mysql_connect()
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    result = []

    for query in res:
        text = query[0]
        words1 = re.sub("[^\w]", " ",  text).split() 
        for str in words1:
            if str == search:
                result.append(query)

    data = pickle.dumps(result)
    r.set("data", data)
    result_redis = pickle.loads(r.get("data"))

    return result_redis


def str_on_page(res):
    result = []
    count = 1
    for query in res:
        clear = "[tweet {}]".format(count)+query[0] 
        result.append(clear)
        count += 1

    return result