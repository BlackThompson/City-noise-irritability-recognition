# -*- encoding: utf-8 -*-

"""
@File    :   audio_processor.py
@Time    :   2021/05/01 14:47:57
@Author  :   silist
@Version :   1.0
@Desc    :   对于每个传入的audio_info
             1. 提取声谱图
             2. 输入模型运算结果
             3. 结果生成pctn_sub_result并存入数据库
             4. 返回结果
"""

import os
from utils.mysqlutils.mysql_singleton import MysqlSingleton
import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from models.pct_sub_result import PctSubResult
from backend.pct_backend import PctBackend
from utils.convertor_utils import parse_output_file_path


class AudioProcessor():
    audio_info = None
    output_path = None

    def __init__(self, audio_info) -> None:
        super().__init__()
        self.audio_info = audio_info

    def input(self, audio_info):
        # if not 
        self.audio_info = audio_info

    def _create_spectrogram(self):
        if not self.audio_info:
            print("[ERROR] AudioProcessor: audio_info is None!")
            return
        input_fp = self.audio_info.file_path
        output_fp = parse_output_file_path(input_fp)
        matplotlib.use('Agg')
        plt.interactive(False)
        clip, sample_rate = librosa.load(self.audio_info.file_path, sr=None)
        fig = plt.figure(figsize=[1.94, 1.94])
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
        plt.savefig(output_fp, dpi=400, bbox_inches='tight', pad_inches=0)
        plt.close()
        fig.clf()
        plt.close(fig)
        plt.close('all')
        self.output_path = output_fp
        del output_fp, input_fp, clip, sample_rate, fig, ax, S

    def _get_result(self):
        if not self.output_path:
            print("[ERROR] AudioProcessor: output_path is None!")
            return
        backend = PctBackend()
        pct_arr = backend.predict(self.output_path)
        res = PctSubResult(os.path.basename(self.audio_info.file_path), float(pct_arr[0, 0]), float(pct_arr[0, 1]),
                           float(pct_arr[0, 2]), self.audio_info.place, self.audio_info.create_time)
        return res

    def process(self):
        self._create_spectrogram()
        res = self._get_result()
        # 插入数据库
        mysql_instance = MysqlSingleton()
        mysql_instance.insert_pct_sub_result(res)
        return res
