#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jackie
#
# Created:     20/01/2013
# Copyright:   (c) Jackie 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Common_Functions import *
"""
PROBLEM 20

n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
def prob20():
    partialFac = 1
    for i in range(1,101):
        partialFac *= i
        if partialFac % 10 == 0:
           partialFac /= 10

    sumS = 0
    while partialFac != 0:
        sumS += partialFac%10
        partialFac /= 10
    return sumS

"""
PROBLEM 21

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b,
 then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def sumOfFactors(n):
    if n ==1:
        return 0
    i = 2
    sumSoFar = 1 # start with 1 (factor of every number)
    li = []
    while i*i <= n:
        if n%i == 0:
            sumSoFar += i
            li.append(i)
            if i*i != n:
                sumSoFar += n/i
                li.append(n/i)
        i+=1
   # print li
    return sumSoFar

def prob21():
    table = {}
    amNums = []

    for i in range(2,10000):
        # put in table if not already in
        if i not in table:
            table[i] = sumOfFactors(i)
        d_i = table[i]
        # only consider if less than 10,000, and not itself
        if d_i < 10000 and i != d_i:
            if d_i not in table:
                table[d_i] = sumOfFactors(d_i)
            compliment = table[d_i]
            if(compliment == i):
                amNums.append(i)
    print amNums
    return sum(n for n in amNums)

"""
PROBLEM 23

A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number.
For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
"""

def prob23():
    s = 0
    # 1 if abundant
    listAbundant = [isAbundant(i) for i in range(28124)]
    for num in range(1,28124):
        if not sumTwoAbundant(num, listAbundant):
            s += num
    return s

def isAbundant(n):
    """returns true if n is abundant"""
    if sumOfFactors(n) > n:
        return 1
    return 0


def sumTwoAbundant(n, listAbundant):
    for i in range(1,n/2+1):
        diff = n -i
        if listAbundant[i] == 1 and listAbundant[diff] == 1:
            return True
    return False


"""
PROBLEM 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

def prob24():
    perm = permutationsDynamic(range(10), {})
    print len(perm)
    print perm[999999]

# give list of permutations, given list li, where li is ordered from
# smallest to largest
# stops when list is larger than a million
def permutations(li, dynDict):
    licopy = li[:]
    listOfLists = []
    if len(li) == 1:
        return [li]
    for first in licopy:
        li.remove(first)
        for sublist in permutationsDynamic(li, dynDict):
            sublist.insert(0,first)
            listOfLists.append(sublist)
        li = licopy[:]
        if len(listOfLists) > 1000000:
            break
    return listOfLists

def permutationsDynamic(li,dynDict):
    if len(li) in dynDict:
        return [[li[i] for i in standList] for standList in dynDict[len(li)]]
    else:
        dynDict[len(li)] = permutations(range(len(li)), dynDict)
        return permutationsDynamic(li, dynDict)

# given a list, return next permutation in lexicographical order
def nextPermutation(perm):
    rev = perm[::-1]
    length = len(perm)
    pivot = 0
    pivValue = rev[0]
    for i in range(length):
        if rev[i] > rev[i+1]:
            pivot = i+1
            pivValue = rev[pivot]
            break
    for i in range(length):
        if rev[i] > rev[pivot]:
            rev[pivot] = rev[i]
            rev[i] = pivValue
            revCopy = rev[:]
            for j in range(pivot):
                rev[j] = revCopy[pivot-j -1]
            break
    return rev[::-1]

def prob24_again():
    curr = range(10)
    for i in range(999999):
        curr = nextPermutation(curr)
    return curr


"""
PROBLEM 25

What is the first term in the Fibonacci sequence to contain 1000 digits?
Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1
"""

def prob25():
    prev = 1
    curr = 1
    nex = 2
    thousandDigits = 10**999
    term = 3
    while nex/thousandDigits == 0:
        prev = curr
        curr = nex
        nex = prev+curr
        term += 1
    return term



"""
PROBLEM 26

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666...,
and has a 1-digit recurring cycle.
 It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
 in its decimal fraction part.

"""

from decimal import Decimal

def prob26():
    maxSoFar = 6
    max_d = 7
    for d in xrange(7,1000):
        rec = lengthCycle(d)
        if rec > maxSoFar:
            maxSoFar = rec
            max_d = d
    return max_d


def lengthCycle(divisor):
    li = []
    remaining_list = []
    dividend = 100
    remaining = -1
    while remaining not in remaining_list[:-1]:
        li.append(dividend/divisor)
        remaining = dividend - li[-1]*divisor
        if remaining == 0:
            return -1
        remaining_list.append(remaining)
        dividend = remaining * 10
    return len(remaining_list) - remaining_list.index(remaining) - 1



"""
PROBLEM 27

Euler published the remarkable quadratic formula:

n? + n + 41

It turns out that the formula will produce 40 primes
for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41? + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n? - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""

def prob27():
    # set up sieve
    largest = 2000
    # sieve is 1 if prime
    sieve = dict((k,1) for k in range(2,2001))
    sieve[1] = 0
    prime = []

    for j in range(2,2001):
        # if not crossed out
        if sieve[j] == 1:
            prime.append(j)
            mul = 1
            while mul*j < 2001:
                sieve[mul*j] = 0
                mul += 1
    maxSoFar = 39
    maxA = 1
    maxB = 41
    a = -999
    while a < 1000:
        for b in prime:
            if b > 1000:
                break
            curr = consPrimes(a,b,prime)
            if curr > maxSoFar:
                maxSoFar = curr
                maxA = a
                maxB = b
            curr = consPrimes(a,-b,prime)
            if curr > maxSoFar:
                maxSoFar = curr
                maxA = a
                maxB = b
        a += 2
    return maxA*maxB

def consPrimes(a,b,prime):
    n = 0
    while (isPrime(n**2 + a*n + b, prime)):
        n+=1
    return n-1

# determines prime given sieve
def isPrime(n,sieve):
    if n in sieve:
        return True
    elif n < 2000:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

"""
PROBLEM 28

Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?

"""

def prob28():
    sumSoFar = 1
    row = 1
    curr = 1
    toAdd = 2
    while row < 501:
        for i in range(4):
            curr += toAdd
            sumSoFar += curr
        toAdd += 2
        row += 1
    return sumSoFar

"""
PROBLEM 29

Consider all integer combinations of ab for 2  a  5 and 2  b  5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed,
we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for
2  a  100 and 2  b  100?

ANSWER: 9183


I think I did this by hand..

Duplicates:
4: 49
8: 49
9: 49
16: 58
25: 49
27: 49
32: 48
36: 49
49: 49
64: 62
81: 58
100: 49

SUM: 618

99*99 - 618 = 9183

"""