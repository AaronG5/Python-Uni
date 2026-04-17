import unittest
from mypackage import rational
from mypackage import perfect

class Perfect_Test(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      cls.known_perfect = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]

   def test_perfect(self):
      for n in self.known_perfect:
         self.assertTrue(perfect(n))

   def test_not_perfect(self):
      for n in range(-100, 10000):
         if n not in self.known_perfect:
            self.assertFalse(perfect(n))

   def test_invalid_input(self):
      for n in ['string', 3.5, -0.0076, [1, 2, 3], (1, 2, 3)]:
         with self.assertRaises(TypeError):
            perfect(n)

class Rational_Test(unittest.TestCase):
   def test_rational_repr(self):
      a = rational(1, 2)
      assert repr(a) == "Rational(1, 2)"
      a = rational(13, 39)
      assert repr(a) == "Rational(1, 3)"

   def test_rational_str(self):
      a = rational(5, 7)
      assert str(a) == "5/7"
      a = rational(8, 6)
      assert str(a) == "4/3"

   def test_rational_add(self):
      a = rational(2, 7)
      b = rational(3, 7)
      c = a.add(b)
      assert repr(c) == "Rational(5, 7)"
      a = rational(5, 6)
      b = rational(3, 14)
      c = a.add(b)
      assert repr(c) == "Rational(22, 21)"

if __name__ == '__main__':
   unittest.main(verbosity=2)