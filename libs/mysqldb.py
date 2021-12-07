
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


def search_database(input):
    input_list = re.sub("@", " ",  input).split() 

    res = mysql_connect()
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    data = pickle.dumps(res)
    r.set("data", data)
    result_redis = pickle.loads(r.get("data"))

    result = []
    for word in input_list:
        for query in result_redis:
            text = query[0]
            words1 = re.sub("@", " ",  text).split() 
            for str in words1:
                if str == word:
                    result.append(query)

    return result


def str_on_page(res):
    result = []
    count = 1
    for query in res:
        clear = "[tweet {}]".format(count)+query[0] 
        result.append(clear)
        count += 1

    return result