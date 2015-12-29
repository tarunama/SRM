# -*- coding: utf-8 -*-
import unittest
from sortness import Sortness


class TestSortness(unittest.TestCase):

    def setUp(self):
        self.case_1 = Sortness([3,2,1,4,6,7,5,8])
        self.case_2 = Sortness([1,2,3])
        self.case_3 = Sortness([5,4,3,2,1])
        self.case_4 = Sortness([1,5,8,7,9,6,10,12,11,3,4,2])

    def test_sortness(self):
        self.assertEqual(self.case_1.get_sortness(), 1.25)
        self.assertEqual(self.case_2.get_sortness(), 0.0)
        self.assertEqual(self.case_3.get_sortness(), 4.0)
        self.assertEqual(self.case_4.get_sortness(), 5.166666666666667)

if __name__ == '__main__':
    unittest.main()
