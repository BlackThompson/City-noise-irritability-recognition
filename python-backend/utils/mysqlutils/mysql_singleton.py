# -*- encoding: utf-8 -*-

"""
@File    :   mysql_pool.py
@Time    :   2021/05/02 11:33:29
@Author  :   silist
@Version :   1.0
@Desc    :   mysql连接单例
"""

import pymysql
import datetime

from utils import config
from utils.wrapper import singleton

@singleton
class MysqlSingleton():
    
    conn = None

    def __init__(self) -> None:
        self.conn = pymysql.connect(host=config.MYSQL_HOST, 
                             port=config.MYSQL_PORT,
                             user=config.MYSQL_USER, 
                             password=config.MYSQL_PWD, 
                             database=config.MYSQL_DB)
    
    def __exit__(self):
        self.conn.close()

    def insert_soundtype_params(self, sp):
        sql = "INSERT INTO `soundtype_params` VALUES ('%s', %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f,\
                %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f,\
                %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %.4f)" % (
                sp.file_name, sp.leq_mean, sp.leq_std, sp.leq_25, sp.leq_median, sp.leq_75, sp.leq_10_90, 
                sp.loudness_mean, sp.loudness_std, sp.loudness_25, sp.loudness_median, sp.loudness_75, 
                sp.loudness_10_90, sp.roughness_mean, sp.roughness_std, sp.roughness_25, sp.roughness_median, 
                sp.roughness_75, sp.roughness_10_90, sp.sharpness_mean, sp.sharpness_std, sp.sharpness_25, 
                sp.sharpness_median, sp.sharpness_75, sp.sharpness_10_90, sp.fluct_mean, sp.fluct_std, 
                sp.fluct_25, sp.fluct_median, sp.fluct_75, sp.fluct_10_90, sp.tonality_mean,  
                sp.tonality_std, sp.tonality_25, sp.tonality_median, sp.tonality_75, sp.tonality_10_90)
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
    
    def insert_pct_sub_result(self, result):
        time_str = datetime.datetime.fromtimestamp(result.create_time / 1e3).strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO `sound_pct_sub` (file_name, pctn, pctu, pctm, create_time, place) VALUES ('%s', %.4f, %.4f, %.4f, '%s', '%s')" % (result.file_name, result.pctn, result.pctu, result.pctm, time_str, result.place)
        # print(sql)
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
