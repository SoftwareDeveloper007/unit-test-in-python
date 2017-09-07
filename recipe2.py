import unittest


class RomanNumericalConverter(object):
    def __init__(self, roman_numerical):
        self.roman_numerical = roman_numerical
        self.digit_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def convert_to_decimal(self):
        val = 0
        for char in self.roman_numerical:
            val += self.digit_map[char]
        return val


class RomanNumericalConverterTest(unittest.TestCase):
    def test_parsing_millenia(self):
        value = RomanNumericalConverter("M")
        self.assertEqual(1000, value.convert_to_decimal())

    def test_parsing_century(self):
        value = RomanNumericalConverter("C")
        self.assertEqual(10, value.convert_to_decimal())

    def test_parsing_half_century(self):
        value = RomanNumericalConverter("M")
        self.assertEqual(50, value.convert_to_decimal())

    def test_parsing_decade(self):
        value = RomanNumericalConverter("M")  
        self.assertEqual(10, value.convert_to_decimal())

    def test_parsing_half_decade(self):
        value = RomanNumericalConverter("M")
        self.assertEqual(5, value.convert_to_decimal())

    def test_parsing_one(self):
        value = RomanNumericalConverter("M")
        self.assertEqual(1, value.convert_to_decimal())

    def test_empty_roman_numeral(self):
        value = RomanNumericalConverter("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)

    def test_no_roman_numeral(self):
        value = RomanNumericalConverter(None)
        self.assertRaises(TypeError, value.convert_to_decimal)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumericalConverter)
    unittest.TextTestRunner(verbosity=2).run(suite)
