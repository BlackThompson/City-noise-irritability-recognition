# -*- encoding: utf-8 -*-

class PctnResult(object):
    def __init__(self, file_name, value, place, create_time) -> None:
        self.file_name = file_name
        self.value = value
        self.place = place
        self.create_time = create_time
    
    def __str__(self) -> str:
        return "[PctnResult]: file_name: %s, value: %s, place: %s, create_time: %s" % (
            self.file_name, self.value, self.place, self.create_time)