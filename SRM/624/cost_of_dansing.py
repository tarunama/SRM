class CostOfDancing(object):

    def __init__(self, d_cost, k):
        self.k = k
        self.d_cost = sorted(d_cost, reverse=True)
        self.ans = 0

    def minimum(self):
        if self.k > 0:
            self.ans += self.d_cost.pop()
            self.k -= 1
            self.minimum()
        else:
            print self.ans

cls = CostOfDancing([1, 5, 3, 4], 2)
cls.minimum() # 4
cls = CostOfDancing([1, 5, 4], 3)
cls.minimum() # 10
cls = CostOfDancing([2, 2, 4, 5, 3], 1)
cls.minimum() # 2
cls = CostOfDancing([973, 793, 722, 573, 521, 568, 845, 674, 595, 310, 284, 794,
913, 93, 129, 758, 108, 433, 181, 163, 96, 932, 703, 989, 884, 420, 615, 991,
364, 657, 421, 336, 801, 142, 908, 321, 709, 752, 346, 656, 413, 629, 801],
39)
cls.minimum() # 20431
