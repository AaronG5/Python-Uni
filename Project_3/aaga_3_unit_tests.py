import unittest
m = __import__('aaga_3')
is_perfect_number = m.is_perfect_number

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

if __name__ == '__main__':
   unittest.main(verbosity=2)