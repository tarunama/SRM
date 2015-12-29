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
