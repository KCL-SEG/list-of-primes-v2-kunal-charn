"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError()
    num = 2
    while(len(list) != number_of_primes):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            list.append(num)
        num = num+1
    return list
