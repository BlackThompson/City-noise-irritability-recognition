# -*- encoding: utf-8 -*-

class PctSubResult():
    def __init__(self, file_name, pctn, pctu, pctm, place, create_time) -> None:
        self.file_name = file_name
        self.pctn = pctn
        self.pctu = pctu
        self.pctm = pctm
        self.place = place
        self.create_time = create_time

    def __str__(self) -> str:
        return "[PctSubResult]: file_name: %s, pctn: %s, pctu: %s, pctm: %s, place: %s, create_time: %s" % (
            self.file_name, self.pctn, self.pctu, self.pctm, self.place, self.create_time)