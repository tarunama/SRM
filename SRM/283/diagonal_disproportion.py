class DiagonalDisproportion(object):

    def __init__(self, matrix):
        self.matrix = [list(s) for s in matrix]
        self.len = len(self.matrix)

    def get_disproportion(self):
        if self.len == 1:
            print 0
            return
        dia = [int(e[0][e[1]]) for e in zip(self.matrix, xrange(self.len))]
        col = [int(e[0][e[1]]) for e in zip(
                                    self.matrix, xrange(self.len-1, -1, -1))]
        print sum(dia) - sum(col)

cls = DiagonalDisproportion(["190","828","373"])
cls.get_disproportion() # 1
cls = DiagonalDisproportion(["9000","0120","0000","9000"])
cls.get_disproportion() # -1
cls = DiagonalDisproportion(["6"])
cls.get_disproportion() # 0
cls = DiagonalDisproportion(["7748297018","8395414567","7006199788","5446757413","2972498628",
"0508396790","9986085827","2386063041","5687189519","7729785238"])
cls.get_disproportion() # -24
