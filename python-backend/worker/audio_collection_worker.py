# -*- encoding: utf-8 -*-

"""
@File    :   audio_collection_work.py
@Time    :   2021/05/03 00:58:30
@Author  :   silist
@Version :   1.0
@Desc    :   从mq接受audio_collection并处理
"""

import json
from models.audio_collection import AudioCollection
import traceback
from multiprocessing import Process
from utils.redisutils.consumer import RedisConsumer
from utils.redisutils.producer import RedisProducer
from processor.audio_collection_processor import AudioCollectionProcessor
from utils.convertor_utils import dict_to_audio_collection, pctn_result_to_dict

class AudioCollectionWorker(Process):

    CONSUME_QUEUE = "audiocollectiontask"
    PRODUCE_QUEUE = "pctnresult"

    def __init__(self):
        super(AudioCollectionWorker, self).__init__()

    def _process_message(self, msg):
        # print("[INPUT]: %s\n\n" % msg)
        pctn_result = None
        try:
            obj = json.loads(msg)
            # print(obj)
            # print(list(obj.keys()))
            audio_collection = AudioCollection(obj['collections'])
            ac_processor = AudioCollectionProcessor(audio_collection=audio_collection)
            pctn_result = ac_processor.process()
        except Exception as e:
            print("[ERROR] AudioCollectionWorker: %s" % e)
            traceback.print_exc()
        return pctn_result

    def _send_message(self, pctn_result):
        if not pctn_result:
            print("[ERROR] AudioCollectionWorker: pctn_result is None!")
            return
        try:
            msg = json.dumps(pctn_result_to_dict(pctn_result))
            producer = RedisProducer(queue=self.PRODUCE_QUEUE)
            producer.produce(msg)
            return True
        except Exception as e:
            print("[ERROR] AudioCollectionWorker: %s" % e)
            traceback.print_exc()
        
        return False
    
    def _pipeline_wrapper(self, msg):
        # print("S1: ", msg)
        pctn_result = self._process_message(msg)
        # print("S2: ", pctn_result)
        return self._send_message(pctn_result)

    def run(self):
        print("Start Audio Collection Worker.")
        consumer = RedisConsumer(queue=self.CONSUME_QUEUE)
        consumer.consume(self._pipeline_wrapper)
