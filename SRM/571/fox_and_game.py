class FoxAndGame(object):

    def __init__(self, str_list):
        self.str_list = str_list

    def count_stars(self):
        return sum([self.count_char(e) for e in self.str_list])

    @staticmethod
    def count_char(element):
        """oの数を数える"""
        return element.count("o")


# tests
f = FoxAndGame(["ooo", "ooo"])
print(f.count_stars())  # 6
f = FoxAndGame(["ooo", "oo-", "o--"])
print(f.count_stars())  # 6
f = FoxAndGame(["ooo", "---", "oo-", "---", "o--"])
print(f.count_stars())  # 6
f = FoxAndGame(["o--","o--","o--","ooo","---"])
print(f.count_stars())  # 6
f = FoxAndGame(["---", "o--","oo-","ooo","ooo","oo-","o--","---"])
print(f.count_stars())  # 12
f = FoxAndGame(["---","---","---","---","---","---"])
print(f.count_stars())  # 0
f = FoxAndGame(["oo-"])
print(f.count_stars())  # 2
