## Synopsis
The solution for a multiplication problem in Karatsuba's Multiplication algorithm can be expressed as follows:

```
x*y = 10n(ac) + 10n/2(ad + bc) + bd
```

Gauss's trick involves computing the middle term *ad + bc* not by finding the terms invidividually, but by finding the product of *(a + b)(c + d)*, which equals *ac + ad + bc + bd*, and then subtracting *ac* and *bd*, which we have to solve for separately anyways. The steps for Karatsuba's Multiplication algorithm can be summarized as follows:

* Recursively compute ac
* Recursively compute bd
* Recursively compute *(a + b)(c + d) = ac + ad + bc + bd*

## Motivation

The motivation for recreating this algorithm is to realize the ingenuity of Gauss's trick which led to one of the more efficient multiplication algorithms used today.

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
