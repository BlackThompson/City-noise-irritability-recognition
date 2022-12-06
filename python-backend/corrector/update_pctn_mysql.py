# -*- encoding: utf-8 -*-

"""
@File    :   update_pctn_mysql.py
@Time    :   2021/07/02 16:44:12
@Author  :   silist
@Version :   1.0
@Desc    :   更新数据库表值
"""

# UPDATE `sound_pctn_new` SET `value`=v WHERE `file_name`=k

import pymysql
import pickle
from tqdm import tqdm


# MYSQL_HOST = "218.17.89.163"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "env"
MYSQL_PWD = "env"
MYSQL_DB = "environment"


class MysqlSingleton():
    
    conn = None


    def __init__(self) -> None:
        self.conn = pymysql.connect(host=MYSQL_HOST, 
                             port=MYSQL_PORT,
                             user=MYSQL_USER, 
                             password=MYSQL_PWD, 
                             database=MYSQL_DB)

    def __exit__(self):
        self.conn.close()

    def update_pctn(self, file_name, new_value):
        sql = "UPDATE `sound_pctn` SET `value`=%.6f WHERE `file_name`=\"%s\"" % (new_value, file_name)
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
        
if __name__ == '__main__':
    d = pickle.load(open("./files/id_avg_pctn_map.dict", "rb"))
    ms = MysqlSingleton()
    success_count = 0
    for _id in tqdm(sorted(list(d.keys()))):
        pctn = d[_id]
        file_name = "Record%d ( 0.00-60.00 s).wav" % _id
        ms.update_pctn(file_name, pctn)
        success_count += 1
    print("[END] success_count:", success_count)
