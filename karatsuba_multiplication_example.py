def karatsuba_mult(x,y,length):

  a = x // (10**(length//2))
  b = x % (10**(length//2))
  c = y // (10**(length//2))
  d = y % (10**(length//2))

  if length==2:
    term1 = a*c
    term2 = b*d
    term3 = (a+b)*(c+d)-term1-term2
    product = 10**length*term1 + term2 + 10**(length//2)*term3
  else:
    term1 = karatsuba_mult(a,c,length//2)
    term2 = karatsuba_mult(b,d,length//2)
    term3 = karatsuba_mult(a+b,c+d,length//2) - term1 -term2
    product = 10**length*term1 + term2 + 10**(length//2)*term3

  return product

x = 8576456798574326;
y = 7465358906879078;
print('3: ', karatsuba_mult(x, y, 16));
