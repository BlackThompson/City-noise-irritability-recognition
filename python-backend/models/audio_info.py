# -*- encoding: utf-8 -*-

class AudioInfo(object):
    def __init__(self, file_path, create_time, place) -> None:
        self.file_path = file_path
        self.create_time = create_time
        self.place = place
