# -*- coding: utf-8 -*-
import unittest
from inside_out import InsideOut


class TestInsideOut(unittest.TestCase):

    def setUp(self):
        self.case_1 = InsideOut("I ENIL SIHTHSIREBBIG S")
        self.case_2 = InsideOut("LEVELKAYAK")
        self.case_3 = InsideOut("H YPPAHSYADILO")
        self.case_4 = InsideOut("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.case_5 = InsideOut(
            "RUT OWT SNEH HCNERF EERHTEGDIRTRAP A DNA  SEVODELT")

    def test_inside_out(self):
        self.assertEqual(self.case_1.unscramble(), "THIS LINE IS GIBBERISH")
        self.assertEqual(self.case_2.unscramble(), "LEVELKAYAK")
        self.assertEqual(self.case_3.unscramble(), "HAPPY HOLIDAYS")
        self.assertEqual(self.case_4.unscramble(),
                        "MLKJIHGFEDCBAZYXWVUTSRQPON")
        self.assertEqual(self.case_5.unscramble(),
                         "THREE FRENCH HENS TWO TURTLEDOVES  AND A PARTRIDGE")


if __name__ == '__main__':
    unittest.main()
