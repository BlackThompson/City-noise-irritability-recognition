# -*- encoding: utf-8 -*-

"""
@File    :   pct_backend.py
@Time    :   2021/05/01 15:03:16
@Author  :   silist
@Version :   1.0
@Desc    :   模型运算后端-pct模型后端
             需要维持单例
"""

import os
import numpy as np
import pandas as pd
from skimage import io, transform
from tensorflow.keras.models import load_model

from utils.wrapper import singleton
from utils import config

@singleton
class PctBackend():
    
    MODEL_PATH = config.PCT_MODEL_PATH

    _model = None
    _input_shape = (224, 224, 3)

    def __init__(self, model_path=None):
        if not model_path:
            model_path = self.MODEL_PATH
        print("Loading PCT Model from %s ..." % model_path)
        self._load_model(model_path)

    def _load_model(self, model_fp):
        self._model = load_model(model_fp)

    def _predict_single_image(self, img_fp):
        if not self._model:
            raise FileNotFoundError('Model is not loaded!')
        if not os.path.exists(img_fp):
            raise FileNotFoundError('Image not exists!')
        print("\033[32m[INFO]\033[0m Loading image from %s ..." % img_fp)
        img = io.imread(img_fp)
        # Skimage Version 0.15!
        # print("\033[32m[INFO]\033[0m Resizing image to %s ..." % self._input_shape)
        img = transform.resize(img, self._input_shape, mode='constant')
        w, h, c = self._input_shape
        img = np.reshape(img, (-1, w, h, c))
        print("\033[32m[INFO]\033[0m Predicting result ...")
        pct = self._model.predict(img)
        return pct

    def _form_pct(self, pct_array):
        pct_array[pct_array < 0] = 0
        pct_array[pct_array > 1] = 1
        for i in range(pct_array.shape[0]):
            pct_array[i] /= pct_array[i].sum()
        return pct_array

    def predict(self, img_fp):
        pct = self._predict_single_image(img_fp)
        return self._form_pct(pct)