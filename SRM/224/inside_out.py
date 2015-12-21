# -*- coding: utf-8 -*-
class InsideOut(object):

    def __init__(self, line):
        self.str_line = line

    def unscramble(self):
        middle = int(len(self.str_line) / 2)
        left = self.str_line[:middle]
        right = self.str_line[middle:]
        return left[::-1] + right[::-1]


# tests
f = InsideOut("I ENIL SIHTHSIREBBIG S")
print(f.unscramble())  # THIS LINE IS GIBBERISH
f = InsideOut("LEVELKAYAK")
print(f.unscramble())  # LEVELKAYAK
f = InsideOut("H YPPAHSYADILO")
print(f.unscramble())  # HAPPY HOLIDAYS6
f = InsideOut("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f.unscramble())  # MLKJIHGFEDCBAZYXWVUTSRQPON
f = InsideOut("RUT OWT SNEH HCNERF EERHTEGDIRTRAP A DNA  SEVODELT")
print(f.unscramble())  # THREE FRENCH HENS TWO TURTLEDOVES  AND A PARTRIDGE
