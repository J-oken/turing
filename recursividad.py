#!/bin/env python3

import sys

# n! = n * (n-1)!
#------------------------------------------------------------------------------
def factorial_i(n):
    r=n;
    while n>1:
          n=n-1;
          r=r*n;
    return r;
    
#------------------------------------------------------------------------------
def factorial_i2(n):
    r=1;
    for i in range(1,n+1):
        r=r*i;
    return r;

#-----------------------------------------------------------
def factorial(n):
    if n==1: return 1;
    else:    return n*factorial(n-1);

#==============================================================================
for i,arg in enumerate(sys.argv):
    if i==0: continue;
    f=factorial(int(arg));
    print(f"El {arg}! es {f}");

