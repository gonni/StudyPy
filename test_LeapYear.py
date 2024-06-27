import LeapYear
import unittest

class TestLeapYear(unittest.TestCase):
    def test_2020(self):
        r = LeapYear.is_leap_year(2021)
        self.assertTrue(r, True)

if __name__ == '__main__':
    unittest.main()