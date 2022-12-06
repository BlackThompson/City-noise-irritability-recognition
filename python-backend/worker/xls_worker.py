# -*- encoding: utf-8 -*-

"""
@File    :   xls_worker.py
@Time    :   2021/05/03 00:57:52
@Author  :   silist
@Version :   1.0
@Desc    :   从mq接受xls_info并处理
"""

import json
from multiprocessing import Process
import traceback

from processor.xls_processor import XlsProcessor
from utils.convertor_utils import dict_to_xls_info, soundtype_result_to_dict
from utils.redisutils.consumer import RedisConsumer
from utils.redisutils.producer import RedisProducer


class XlsWorker(Process):

    CONSUME_QUEUE = "xlstask"
    PRODUCE_QUEUE = "soundtyperesult"


    def __init__(self):
        super(XlsWorker, self).__init__()

    def _process_message(self, msg):
        soundtype_result = None
        try:
            # 反序列化成XlsInfo对象
            xls_info = json.loads(msg, object_hook=dict_to_xls_info)
            print("??", xls_info)
            # 传入XlsProcessor处理
            xls_processor = XlsProcessor(xls_info=xls_info)
            # 得到结果对象
            soundtype_result = xls_processor.process()
        except Exception as e:
            print(msg)
            print("[ERROR] XlsWorker: %s" % e)
            traceback.print_exc()
        return soundtype_result

    def _send_message(self, soundtype_result):
        if not soundtype_result:
            print("[ERROR] XlsWorker: soundtype_result is None!")
            return
        try:
            msg = json.dumps(soundtype_result_to_dict(soundtype_result))
            producer = RedisProducer(queue=self.PRODUCE_QUEUE)
            producer.produce(msg)
            return True
        except Exception as e:
            print("[ERROR] XlsWorker: %s" % e)
            traceback.print_exc()
        
        return False
    
    def _pipeline_wrapper(self, msg):
        soundtype_result = self._process_message(msg)
        return self._send_message(soundtype_result)

    def run(self):
        print("Start Xls Worker.")
        consumer = RedisConsumer(queue=self.CONSUME_QUEUE)
        consumer.consume(self._pipeline_wrapper)
