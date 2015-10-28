import string


class WritingsWords(object):

    def __init__(self, word):
        self.word = word
        alpha_num = zip(string.uppercase, [i for i in xrange(1,27)])
        self.alphas = {key: value for (key, value) in alpha_num}

    def write(self):
        return sum([self.alphas.get(c) for c in self.word])


ww = WritingsWords("A")
print ww.write() # 1
ww = WritingsWords("ABC")
print ww.write() # 6
ww = WritingsWords("VAMOSGIMNASIA")
print ww.write() # 143
ww = WritingsWords("TOPCODER")
print ww.write() # 96
ww = WritingsWords("SINGLEROUNDMATCH")
print ww.write() # 183
ww = WritingsWords("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
print ww.write() # 1300
