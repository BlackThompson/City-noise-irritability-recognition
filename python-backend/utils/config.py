# -*- encoding: utf-8 -*-

"""
@File    :   config.py
@Time    :   2021/05/02 11:24:06
@Author  :   silist
@Version :   1.0
@Desc    :   配置文件
"""

# 声谱图输出目录
SPECTROGRAM_OUTPUT_FOLDER = "{input}/spec"

# 模型文件地址
PCT_MODEL_PATH = "./files/pct_model.h5"
SOUNDTYPE_MODEL_PATH = "./files/soundtype_model.pkl"

# redis连接配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# mysql连接配置
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "zjkj"
MYSQL_DB = "environment"
