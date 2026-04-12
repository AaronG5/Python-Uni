# 8 uzduotis: patikrinti ar skaičius yra tobulas

import math

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

def main():
   import doctest
   doctest.testmod(verbose=True)
   return 1


if __name__ == '__main__':
   main()