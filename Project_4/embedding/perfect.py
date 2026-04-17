import math

def is_perfect(n):
   if not isinstance(n, int):
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