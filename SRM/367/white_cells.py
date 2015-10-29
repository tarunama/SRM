# not solve

class WhiteCells(object):

    def __init__(self, boards):
        self.boards = boards
        self.counter = None
        self.result = 0

    def count_occupied(self):
        for board in self.boards:
            self.counter = 0
            for cell in board:
                if self.counter % 2 == 0:
                    print cell
                    if cell == "F":
                        self.result += 1
                self.counter += 1
        return self.result

ww = WhiteCells(
["........","........",
"........","........",
"........","........",
"........","........"]
)
print ww.count_occupied() # 0
ww = WhiteCells(
["FFFFFFFF","FFFFFFFF",
 "FFFFFFFF","FFFFFFFF",
 "FFFFFFFF","FFFFFFFF",
 "FFFFFFFF","FFFFFFFF"]
)
print ww.count_occupied() # 32
ww = WhiteCells(
[".F.F...F","F...F.F.",
 "...F.F.F","F.F...F.",
 ".F...F..","F...F.F.",
 ".F.F.F.F","..FF..F."])
print ww.count_occupied() # 11
