/*
x*y = 10^n * (ac) + 10^n/2 * (ad + bc) + bd
In a previous example with 4-digit numbers, there were 4 recursive calls to compute the 4 products necessary for computing the final product.
However, since we simply care about the sum of ad and bc, we can do this in 3 operations for Karatsuba’s algorithm:
1. Recursively compute ac
2. Recursively compute bd
3. Recursively compute the product of (a + b)(c + d) = ac + ad + bc + bd

Assumes x and y are of equal length
Assumes x and y have a number of digits that is a power of 2
*/
function karatsuba(x, y, len) {
  var xStr = x.toString();
  var yStr = y.toString();
  if (len <= 2) return x*y;

  var halfLen = Math.floor(len / 2);
  var a = Number(xStr.slice(0, halfLen));
  var b = Number(xStr.slice(halfLen));
  var c = Number(yStr.slice(0, halfLen));
  var d = Number(yStr.slice(halfLen));

  var ac = karatsuba(a, c, halfLen);
  var bd = karatsuba(b, d, halfLen);
  var sumAdBc = karatsuba(a+b, c+d, halfLen) - bd - ac;

  return Math.pow(10,len)*ac + Math.pow(10,halfLen)*sumAdBc + bd;
}

var x = 8576456798574326;
var y = 7465358906879078;
console.log('correct: ', x*y);
console.log('karatsuba: ', karatsuba(x, y, 16));
