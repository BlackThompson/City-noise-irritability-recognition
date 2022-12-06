# -*- encoding: utf-8 -*-

"""
@File    :   xls_processor.py
@Time    :   2021/04/19 10:47:39
@Author  :   silist
@Version :   1.0
@Desc    :   对于每个传入的xls_info
             1. 提取特征
             2. 特征生成soundtype_params
             3. 特征传入模型计算得soundtype_result
"""

from models.xls_info import XlsInfo
from models.soundtype_result import SoundtypeResult
from backend.soundtype_backend import SoundtypeBackend
import os

import numpy as np
import xlrd
from models.soundtype_params import SoundtypeParams
from utils.mysqlutils.mysql_singleton import MysqlSingleton

import warnings

warnings.filterwarnings("ignore")


class XlsProcessor():
    xls_info = None

    def __init__(self, xls_info) -> None:
        super().__init__()
        self.xls_info = xls_info

    def input(self, xls_info):
        self.xls_info = xls_info

    def _extract_params(self):
        if not self.xls_info:
            print("[ERROR] XlsProcessor: xls_info is None!")
            return
        # load excel
        wb = xlrd.open_workbook(self.xls_info.file_path)
        params_dict = {}
        for idx in range(6):
            sheet = wb.sheet_by_index(idx)
            print("!!!Tab", idx)
            param_type = sheet.cell(10, 1).value
            if param_type == 'pressure':
                param_type = 'leq'
            elif param_type == 'fluctuation strength':
                param_type = 'fluct'
            else:
                param_type = param_type.lower()
            values = []
            for i in range(15, min(sheet.nrows, 65521)):
                values.append(float(sheet.cell(i, 1).value))
            values = np.array(values)
            mean = values.mean()
            var = values.var()
            std = values.std(ddof=1)
            max = values.max()
            p_10 = np.percentile(values, 10, interpolation='midpoint')
            p_25 = np.percentile(values, 25, interpolation='midpoint')
            p_50 = np.percentile(values, 50, interpolation='midpoint')
            p_75 = np.percentile(values, 75, interpolation='midpoint')
            p_90 = np.percentile(values, 90, interpolation='midpoint')
            p_10_90 = p_90 - p_10

            params_dict["%s_mean" % param_type] = mean
            params_dict["%s_var" % param_type] = var
            params_dict["%s_std" % param_type] = std
            params_dict["%s_max" % param_type] = max
            params_dict["%s_10" % param_type] = p_10
            params_dict["%s_25" % param_type] = p_25
            params_dict["%s_median" % param_type] = p_50
            params_dict["%s_75" % param_type] = p_75
            params_dict["%s_90" % param_type] = p_90
            params_dict["%s_10_90" % param_type] = p_10_90

        soundtype_params = None
        try:
            file_name = os.path.basename(self.xls_info.file_path).replace("xlsx", "wav")
            print(file_name, "!!!???")
            leq_mean = params_dict["leq_mean"]
            leq_std = params_dict["leq_std"]
            leq_25 = params_dict["leq_25"]
            leq_median = params_dict["leq_median"]
            leq_75 = params_dict["leq_75"]
            leq_10_90 = params_dict["leq_10_90"]
            loudness_mean = params_dict["loudness_mean"]
            loudness_std = params_dict["loudness_std"]
            loudness_25 = params_dict["loudness_25"]
            loudness_median = params_dict["loudness_median"]
            loudness_75 = params_dict["loudness_75"]
            loudness_10_90 = params_dict["loudness_10_90"]
            roughness_mean = params_dict["roughness_mean"]
            roughness_std = params_dict["roughness_std"]
            roughness_25 = params_dict["roughness_25"]
            roughness_median = params_dict["roughness_median"]
            roughness_75 = params_dict["roughness_75"]
            roughness_10_90 = params_dict["roughness_10_90"]
            sharpness_mean = params_dict["sharpness_mean"]
            sharpness_std = params_dict["sharpness_std"]
            sharpness_25 = params_dict["sharpness_25"]
            sharpness_median = params_dict["sharpness_median"]
            sharpness_75 = params_dict["sharpness_75"]
            sharpness_10_90 = params_dict["sharpness_10_90"]
            fluct_mean = params_dict["fluct_mean"]
            fluct_std = params_dict["fluct_std"]
            fluct_25 = params_dict["fluct_25"]
            fluct_median = params_dict["fluct_median"]
            fluct_75 = params_dict["fluct_75"]
            fluct_10_90 = params_dict["fluct_10_90"]
            tonality_mean = params_dict["tonality_mean"]
            tonality_std = params_dict["tonality_std"]
            tonality_25 = params_dict["tonality_25"]
            tonality_median = params_dict["tonality_median"]
            tonality_75 = params_dict["tonality_75"]
            tonality_10_90 = params_dict["tonality_10_90"]

            soundtype_params = SoundtypeParams(file_name, leq_mean, leq_std, leq_25, leq_median, leq_75, leq_10_90,
                                               loudness_mean, loudness_std, loudness_25, loudness_median, loudness_75,
                                               loudness_10_90, roughness_mean, roughness_std, roughness_25,
                                               roughness_median, roughness_75, roughness_10_90, sharpness_mean,
                                               sharpness_std, sharpness_25, sharpness_median, sharpness_75,
                                               sharpness_10_90, fluct_mean, fluct_std, fluct_25, fluct_median, fluct_75,
                                               fluct_10_90, tonality_mean, tonality_std, tonality_25, tonality_median,
                                               tonality_75, tonality_10_90)
            print("aaa", soundtype_params)
        except Exception as e:
            print("[ERROR] XlsProcessor: %s" % e)

        return soundtype_params

    def process(self):
        soundtype_params = self._extract_params()
        if not soundtype_params:
            print("[ERROR] XlsProcessor: soundtype_params is None!")
            return
        # 存入数据库
        mysql_instance = MysqlSingleton()
        mysql_instance.insert_soundtype_params(soundtype_params)
        print("[INFO] XlsProcessor: save soundtype_params  for %s to mysql." % soundtype_params.file_name)
        # 传入后端模型
        input_arr = np.array(
            [soundtype_params.leq_mean, soundtype_params.leq_std, soundtype_params.leq_25, soundtype_params.leq_median,
             soundtype_params.leq_75, soundtype_params.leq_10_90, soundtype_params.loudness_mean,
             soundtype_params.loudness_std, soundtype_params.loudness_25, soundtype_params.loudness_median,
             soundtype_params.loudness_75, soundtype_params.loudness_10_90, soundtype_params.roughness_mean,
             soundtype_params.roughness_std, soundtype_params.roughness_25, soundtype_params.roughness_median,
             soundtype_params.roughness_75, soundtype_params.roughness_10_90, soundtype_params.sharpness_mean,
             soundtype_params.sharpness_std, soundtype_params.sharpness_25, soundtype_params.sharpness_median,
             soundtype_params.sharpness_75, soundtype_params.sharpness_10_90, soundtype_params.fluct_mean,
             soundtype_params.fluct_std, soundtype_params.fluct_25, soundtype_params.fluct_median,
             soundtype_params.fluct_75, soundtype_params.fluct_10_90, soundtype_params.tonality_mean,
             soundtype_params.tonality_std, soundtype_params.tonality_25, soundtype_params.tonality_median,
             soundtype_params.tonality_75, soundtype_params.tonality_10_90])

        backend = SoundtypeBackend()
        res = backend.predict(input_arr)
        soundtype_result = SoundtypeResult(soundtype_params.file_name, int(res[0]), self.xls_info.place,
                                           self.xls_info.create_time)
        return soundtype_result
