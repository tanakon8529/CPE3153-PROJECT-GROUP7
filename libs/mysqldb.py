
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


def split_words(input):
    input_list = re.sub("@", " ",  input).split() 
    return input_list


def sentence_query(input, result):
    result_currect = []
    for sentence in result:
        split_st = set(split_words(sentence[0]))
        split_ip = set(split_words(input))
        result = split_st.intersection(split_ip)
        if len(result) == 3:
            result_currect.append(sentence)

    return result_currect

def word_query(input, data):
    word_current = []
    for query in data:
        text = query[0]
        words1 = re.sub("@", " ",  text).split() 
        for str in words1:
            if str == input:
                word_current.append(query)
    
    return word_current

def search_database(input):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    try:
        res = mysql_connect()
        data = pickle.dumps(res)
        r.set("data", data)
        result_redis = pickle.loads(r.get("data"))
    except:
        result_redis = pickle.loads(r.get("data"))

    input_list = split_words(input)
    if len(input_list) > 1:
        result = sentence_query(input, result_redis)
    else:
        result = word_query(input, result_redis)

    return result


def str_on_page(res):
    result = []
    count = 1
    for query in res:
        clear = "[tweet {}]".format(count)+query[0] 
        result.append(clear)
        count += 1

    return result