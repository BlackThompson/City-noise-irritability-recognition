# -*- encoding: utf-8 -*-

"""
@File    :   audio_collection_processor.py
@Time    :   2021/05/01 14:46:27
@Author  :   silist
@Version :   1.0
@Desc    :   对于每个传入的audio_collection
             1. 遍历其中的audio_info
             2. 传入AudioProcessor处理
             3. 汇总所有pct_sub_result得到pctn_result
"""

from models.pctn_result import PctnResult
import os

from processor.audio_processor import AudioProcessor


class AudioCollectionProcessor():
    audio_collection_info = None
    pct_sub_result_list = []

    def __init__(self, audio_collection) -> None:
        self.audio_collection_info = audio_collection

    def input(self, audio_collection):
        self.audio_collection_info = audio_collection

    def _process_all_audio_info(self):
        for audio_info in self.audio_collection_info.collections:
            processor = AudioProcessor(audio_info)
            pct_sub_res = processor.process()
            if not pct_sub_res:
                print("[ERROR] AudioCollectionProcessor: pct_sub_result is None!")
                continue
            self.pct_sub_result_list.append(pct_sub_res)

    def _get_result(self):
        if len(self.pct_sub_result_list) == 0:
            print("[ERROR] AudioCollectionProcessor: pct_sub_result_list is Empty!")
            return
        # print("===========================================\n[LEN] pct_sub_result_list:")
        # print(len(self.pct_sub_result_list))
        # print("=[VALUE] pct_sub_result_list:")
        # print(self.pct_sub_result_list)
        pctn_avg = sum([x.pctn for x in self.pct_sub_result_list]) / len(self.pct_sub_result_list)
        # print(pctn_avg)
        # print("===========================================\n")
        # print("\n ac len: %s" % len(self.audio_collection_info.collections))
        # print("\n audio_info[0]: %s" % self.audio_collection_info.collections[0].file_path)
        # print("\n audio_info[-1]: %s" % self.audio_collection_info.collections[-1].file_path)
        audio_info = self.audio_collection_info.collections[0]
        file_name = os.path.basename(audio_info.file_path)
        file_name = file_name[:file_name.rfind('-')] + ".wav"
        place = audio_info.place
        create_time = audio_info.create_time
        # print("\n\nfile+name: %s\n\n" % file_name)
        return PctnResult(file_name, pctn_avg, place, create_time)

    def _clear(self):
        self.audio_collection_info = None
        self.pct_sub_result_list.clear()
        # print("after clear: len: %s" % len(self.pct_sub_result_list))

    def process(self):
        self._process_all_audio_info()
        res = self._get_result()
        self._clear()
        return res
