class Soccer(object):

    def __init__(self, wins, ties):
        self.wins = wins
        self.ties = ties
        self.ans = 0

    def max_points(self):
        points = [t[0]*3 + t[1] for t in zip(self.wins, self.ties)]
        print max(points)


cls = Soccer([1,4,3,0,0], [3,1,5,3,1])
cls.max_points() # 14
cls = Soccer([12,45,20,17,48,0], [48,10,53,94,0,100])
cls.max_points() # 145
cls = Soccer([35,0], [0,76])
cls.max_points() # 105
cls = Soccer([0,0,0,0], [0,0,0,0])
cls.max_points() # 0
cls = Soccer(
    [13,79,26,73,14,89,71,37,89,71,19,59,39],
    [88,27,5,70,84,94,20,50,2,11,31,22,50],
)
cls.max_points() # 361
