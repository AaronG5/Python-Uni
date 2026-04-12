# 8 uzduotis: patikrinti ar skaičius yra tobulas

import math
import unittest

def is_perfect_number(n):
   """
      >>> is_perfect_number(-6)
      False
      >>> is_perfect_number(1)
      False
      >>> is_perfect_number(6)
      True
      >>> is_perfect_number(10)
      False
      >>> is_perfect_number(28)
      True
      >>> is_perfect_number(100000)
      False
      >>> is_perfect_number(33550336)
      True
      >>> is_perfect_number('str')
      Traceback (most recent call last):
      ...
      TypeError: Incorrect value type for argument
      >>> is_perfect_number(True)
      Traceback (most recent call last):
      ...
      TypeError: Incorrect value type for argument
   """
   if not isinstance(n, int) or isinstance(n, bool):
      raise TypeError('Incorrect value type for argument')
   if n < 2:
      return False
   
   s = 1
   for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
         s += i
         if i != n // i:
            s += n // i
   return s == n

class Is_Perfect_Number_Test(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      cls.known_perfect = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]

   def test_perfect(self):
      for n in self.known_perfect:
         self.assertTrue(is_perfect_number(n))

   def test_not_perfect(self):
      for n in range(-100, 10000):
         if n not in self.known_perfect:
            self.assertFalse(is_perfect_number(n))

   def test_invalid_input(self):
      for n in ['string', True, False, 3.5, -0.0076, [1, 2, 3], (1, 2, 3)]:
         with self.assertRaises(TypeError):
            is_perfect_number(n)

def main():
   import doctest
   doctest.testmod(verbose=True)
   return 1

if __name__ == '__main__':
   # main()
   unittest.main(verbosity=2)