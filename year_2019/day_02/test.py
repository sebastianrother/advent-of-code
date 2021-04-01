import unittest
from year_2019.day_02.solution import Solution

class TestDay02(unittest.TestCase):
    def test_part01_example01(self):
        input = '1,9,10,3,2,3,11,0,99,30,40,50'
        self.assertEqual(Solution(input).part_1(), 3500)

    def test_part01_example02(self):
        input = '1,0,0,0,99'
        self.assertEqual(Solution(input).part_1(), 2)

    def test_part01_example03(self):
        input = '2,3,0,3,99'
        self.assertEqual(Solution(input).part_1(), 2)

    def test_part01_example04(self):
        input = '2,4,4,5,99,0'
        self.assertEqual(Solution(input).part_1(), 2)

    def test_part01_example05(self):
        input = '1,1,1,4,99,5,6,0,99'
        self.assertEqual(Solution(input).part_1(), 30)
