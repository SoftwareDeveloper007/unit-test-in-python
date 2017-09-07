import unittest


class RomanNumericalConverter(object):
    def __init__(self):
        self.digit_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def convert_to_decimal(self, roman_numerical):
        val = 0
        for char in roman_numerical:
            val += self.digit_map[char]
        return val


class RomanNumericalConverterTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumericalConverter()

    def test_parsing_millenia(self):
        self.assertEqual(1000, self.cvt.convert_to_decimal("M"))

    def test_parsing_century(self):
        self.assertEqual(100, self.cvt.convert_to_decimal("C"))

class RomanNumeralComboTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumericalConverter()

    def test_multi_millenia(self):
        self.assertEqual(4000, self.cvt.convert_to_decimal("MMMM"))

    def test_multi_add_up(self):
        self.assertEqual(2010, self.cvt.convert_to_decimal("MMX"))

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(RomanNumericalConverterTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralComboTest)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
