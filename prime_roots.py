# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 03:13:40 2022

@author: 17
"""

import numpy
import math
import sys
import os


def sort_list_sqr_primes(primes, f):
    primes_and_roots = []
    for n in primes:
        primes_and_roots.append((n, f(n))

def bisection_sqr(prime):
    
    high = prime
    low = 0
    guess = (high + low) / 2.0
    epsilon = 0.0001
    while((guess ** 2 - prime) >= epsilon):
        if guess ** 2 > prime:
            high = guess
        elif guess ** 2 < prime:
            low = guess
        guess = (high + low) / 2.0

def return_100_primes():
    primes = []
    for n in range(1000, 2, -1):
        for x in range(2, n, 1):
            if n % x == 0:
                break
            elif (n % x != 0) and (n in primes) == False:
                primes.append(n)
    return primes
def main():
    
    primes = return_100_primes()
    
if __name__ == "__main__": main()