# -*- encoding: utf-8 -*-

"""
@File    :   pipeline.py
@Time    :   2021/05/03 13:01:05
@Author  :   silist
@Version :   1.0
@Desc    :   实际流水线
"""

from worker.audio_collection_worker import AudioCollectionWorker
from worker.xls_worker import XlsWorker

if __name__ == "__main__":
    print("Start python backend")
    xls_proc = XlsWorker()
    xls_proc.start()

    audio_collection_proc = AudioCollectionWorker()
    audio_collection_proc.start()

    xls_proc.join()
    audio_collection_proc.join()
    print("End Process.")
