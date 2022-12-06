# -*- encoding: utf-8 -*-

"""
@File    :   soundtype_backend.py
@Time    :   2021/05/01 15:02:45
@Author  :   silist
@Version :   1.0
@Desc    :   模型运算后端-声音类型（陶志祥）
             需要维持单例
"""

import joblib
from sklearn.preprocessing import normalize
from utils import config
from utils.wrapper import singleton

@singleton
class SoundtypeBackend():
    
    MODEL_PATH = config.SOUNDTYPE_MODEL_PATH

    _model = None

    def __init__(self, model_path=None) -> None:
        if not model_path:
            model_path = self.MODEL_PATH
        print("Loading Soundtype Model from %s ..." % model_path)
        self._load_model(model_path)
    
    def _load_model(self, model_path):
        self._model = joblib.load(model_path)

    def predict(self, arr):
        arr = arr.reshape(1, -1)
        arr = normalize(arr, norm='l2')
        return self._model.predict(arr)
