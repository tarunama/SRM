# -*- coding: utf-8 -*-
class InsideOut(object):

    def __init__(self, line):
        self.str_line = line

    def unscramble(self):
        middle = int(len(self.str_line) / 2)
        left = self.str_line[:middle]
        right = self.str_line[middle:]
        return left[::-1] + right[::-1]

