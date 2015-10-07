class CheckFunction(object):

    def __init__(self, input_str):
        self.input_lst = [int(n) for n in input_str]
        self.dashes = {
            '0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3,
            '8': 7, '9': 6
        }
        self.total = 0

    def new_function(self):
        for n in self.input_lst:
            self.total += self.dashes[str(n)]
        print self.total


cls = CheckFunction("13579")
cls.new_function() # 21
cls = CheckFunction("02468")
cls.new_function() # 28
cls = CheckFunction("73254370932875002027963295052175")
cls.new_function() # 157
