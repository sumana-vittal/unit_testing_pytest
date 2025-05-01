import unittest

from sqlalchemy import result_tuple

from calculator import Calculator

class TestCalculator(unittest.TestCase):

   def setUp(self):
       #"Set up instance before each test"
        self.calc = Calculator()

   def test_add(self):
        result = self.calc.add(6,6)
        self.assertEqual(result, 12)

   def test_add_failure(self):
        result = self.calc.add(6,6)
        self.assertEqual(result, 17)

   def test_subtract(self):
        result = self.calc.subtract(50,10)
        self.assertEqual(result, 40)

   def test_multiply(self):
        result = self.calc.multiply(6,5)
        self.assertEqual(result, 30)

   def test_divide(self):
        result = self.calc.divide(48,6)
        self.assertEqual(result, 8)

   def test_divide_zero(self):
       with self.assertRaises(ValueError):
           self.calc.divide(10,0)

   def tearDown(self):
       "Clean up"
       pass



