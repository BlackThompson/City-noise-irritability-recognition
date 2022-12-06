# -*- encoding: utf-8 -*-

"""
@File    :   wrapper.py
@Time    :   2021/05/01 15:16:29
@Author  :   silist
@Version :   1.0
@Desc    :   单例装饰器
"""

def singleton(cls):
    _instances = {}

    def getinstance(*args, **kwargs):
        if not cls in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    
    return getinstance
