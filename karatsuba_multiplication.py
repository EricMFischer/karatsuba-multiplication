# Assumes x and y are of equal length
# Assumes x and y have a number of digits that is a power of 2

def karatsuba(x, y, length):
  a = x // 10**(length//2)9
  b = x % 10**(length//2)
  c = y // 10**(length//2)
  d = y % 10**(length//2)

  if (length == 2):
    return x*y

  ac = karatsuba(a, c, length//2)
  bd = karatsuba(b, d, length//2)
  sumAdBc = karatsuba(a+b, c+d, length//2) - bd - ac
  
  return 10**length*ac + 10**(length//2)*sumAdBc + bd
  
  
  
x = 3141592653589793238462643383279502884197169399375105820974944592;
y = 2718281828459045235360287471352662497757247093699959574966967627;
print('1: ', x*y);
print('2: ', karatsuba(x, y, 16));
