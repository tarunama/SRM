class GreaterGameDiv2(object):

    def __init__(self, snuke, sothe):
        self.snuke = snuke
        self.sothe = sothe

    def calc(self):
        cards = zip(self.snuke, self.sothe)
        return len([snuke for snuke, sothe in cards if snuke > sothe])


g = GreaterGameDiv2([1, 3], [4, 2])
print g.calc()
g = GreaterGameDiv2([1,3,5,7,9], [2,4,6,8,10])
print g.calc()
g = GreaterGameDiv2([2], [1])
print g.calc()
g = GreaterGameDiv2([3,5,9,16,14,20,15,17,13,2], [6,18,1,8,7,10,11,19,12,4])
print g.calc()
