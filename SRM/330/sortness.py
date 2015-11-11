from __future__ import division


class Sortness(object):

    def __init__(self, num_list):
        self.num_list = num_list

    def get_sortness(self):
        ret = []
        for n in self.num_list:
            idx = self.num_list.index(n)
            l_list = self.num_list[:idx]
            r_list = self.num_list[idx:]
            ret.append(
                len([e for e in l_list if n < e]) + \
                len([e for e in r_list if n > e])
            )
        return sum(ret) / len(ret)

# tests
s = Sortness([3,2,1,4,6,7,5,8])
print s.get_sortness() # 1.25
s = Sortness([1,2,3])
print s.get_sortness() # 0.0
s = Sortness([5,4,3,2,1])
print s.get_sortness() # 4.0
s = Sortness([1,5,8,7,9,6,10,12,11,3,4,2])
print s.get_sortness() # 5.16666666667
