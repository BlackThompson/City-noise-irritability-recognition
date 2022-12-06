# -*- encoding: utf-8 -*-

from models.audio_info import AudioInfo


class AudioCollection(object):
    collections = []

    def __init__(self, collections) -> None:
        # print("[!AudioCollection] :: ", collections)
        self.collections = []
        for c in collections:
            info = AudioInfo(c['filePath'], c['createTime'], c['place'])
            self.collections.append(info)
