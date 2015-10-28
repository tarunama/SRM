class Drbalance(object):

    def lesscng(self, s, k):
        if k == 0:
            print 0
            return
        ls = [s for s in s]
        p_ts = ls.count('+')
        n_ts = ls.count('-')
        
        if p_ts >= n_ts:
            tms = n_ts
            src = '+'
            chg = '-'
        else:
            tms = p_ts
            src = '-'
            chg = '+'

        for _ in xrange(tms):
            ls.remove('+')
            ls.remove('-')

        ls.remove('-')
        c = len(ls)
        t = 0
        while c != 0:
            c -= 2
            t += 1

        print t

cls = Drbalance()
cls.lesscng("+-+----", 3) # 1
