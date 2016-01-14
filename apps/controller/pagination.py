# -*- coding: utf-8 -*-
import math

class pagination:
    def __init__(self, total,page):
        self.total = total
        self.calculate = float(float(self.total) / 8)
        self.total_page = math.ceil(self.calculate)
        self.page = page
        self.count = float(math.ceil(float(self.page)/8))

    def up(self):
        if self.total_page > self.count*8:
            self.total_page = self.count * 8
            up = int(self.total_page+1)

        else:
            up = int(self.total_page)

        return up


    def down(self):
        if self.count ==1:
            down=1
        else:
            down = int((self.count-1) * 8)

        return down


    def totalCount(self):
        total = range(1+(8*(int(self.count)-1)), int(self.total_page+1))

        return total