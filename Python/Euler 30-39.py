#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jackie
#
# Created:     22/01/2013
# Copyright:   (c) Jackie 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Common_Functions import *
"""
PROBLEM 30

Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.

"""
def prob30():
    sumSoFar = 0
    for i in range(1,531441):
        if sumFifthPower(i) == i:
            sumSoFar += i
    return sumSoFar

def sumFifthPower(n):
    sumSoFar = 0
    while n != 0:
        digit = n%10
        sumSoFar += digit**5
        n /= 10
    return sumSoFar

"""
PROBLEM 31

In England the currency is made up of pound, ?,
and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, ?1 (100p) and ?2 (200p).
It is possible to make ?2 in the following way:

1?1 + 150p + 220p + 15p + 12p + 31p
How many different ways can ?2 be made using any number of coins?
"""

# tried to use dynamic programming but failed.
# dynamic programming must store
# dict[a, b] = number of ways to represent b pence using coins
# whose nominations are less than or equal to coins[a]
def prob31():
    table = dict((i, -1) for i in range(0,201))
    coins = [1,2,5,10,20,50,100,200]
    answer = recurse(200,table,coins,201)
   # print table
    return answer

def recurse(amount,table,coins,lastCoin):
    if amount == 0:
        return 1
    sumSoFar = 0
    liCoins = [c for c in coins if c <= lastCoin and c <= amount]
    liCoins.reverse()
    for coin in liCoins:
        #print coin
        #if table[amount-coin] == -1:
            #table[amount-coin] = recurse(amount-coin,table,coins,coin)
        sumSoFar += recurse(amount-coin,table,coins,coin)
    return sumSoFar


"""
PROBLEM 32

We shall say that an n-digit number is pandigital if it makes
 use of all the digits 1 to n exactly once;
 for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# brute force. can probably be done faster but still O(n)
def prob32():
    sumOfProducts = 0
    for i in range(1000,10000):
        for factor in factors(i):
            if pandigital(factor,i):
                sumOfProducts += i
                break
    return sumOfProducts

def factors(i):
    listFactors = []
    j = 1
    while j*j <= i:
        if j*j == i:
            listFactors.append(j)
            return listFactors
        if i%j == 0:
            listFactors.append(j)
        j+=1
    return listFactors

def pandigital(factor,num):
    digits = range(1,10)
    fac2 = num/factor
    while num != 0:
        digit = num%10
        if digit not in digits:
            return False
        digits.remove(digit)
        num /= 10
    while factor != 0:
        digit = factor%10
        if digit not in digits:
            return False
        digits.remove(digit)
        factor /= 10
    while fac2 != 0:
        digit = fac2%10
        if digit not in digits:
            return False
        digits.remove(digit)
        fac2 /= 10
    # if there are still digits remaining
    if digits:
        return False
    return True

"""
PROBLEM 33

The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting to simplify
it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its
lowest common terms, find the value of the denominator.
"""
def prob33():
    listNums  = 1   # product of numerators
    listDenoms = 1  # product of denominators
    for denom in range(10,100):
        for num in range(10,denom+1):
            if simplifyWrong(num,denom):
                listNums *= num
                listDenoms*=denom
    return simplify(listNums,listDenoms)

def simplifyWrong(num,denom):
    if num == denom:
        return False
    origFrac = simplify(num,denom)
    if tensDigit(num) == onesDigit(denom):
        if origFrac == simplify(onesDigit(num),tensDigit(denom)):
            return True
    if onesDigit(num) == tensDigit(denom):
        if origFrac == simplify(tensDigit(num),onesDigit(denom)):
            return True
    return False

def gcf(num1,num2):
    a = num1
    b = num2
    while (a != 0):
        temp = a
        a = b%a
        b = temp
    return b
def tensDigit(num):
    return (num/10)%10
def onesDigit(num):
    return num%10
def simplify(num,denom):
    factor = gcf(num,denom)
    return [num/factor, denom/factor]


"""
PROBLEM 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the
sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included
"""
from math import factorial

def prob34():
    sumSoFar = 0
    for i in range(10,2540160):
        if factorialDigits(i) == i:
            sumSoFar += i
    return sumSoFar


def factorialDigits(num):
    sumSoFar = 0
    while num != 0:
        digit = num%10
        sumSoFar += factorial(digit)
        num /= 10
    return sumSoFar

"""
PROBLEM 35

The number, 197, is called a circular prime
because all rotations of the digits: 197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def prob35():
# sieve of Eratosthenes
    largest = 1000000
    # listP is 1 if prime
    listP = [1] * 1000000
    listP[0] = 0
    listP[1] = 0
    primes = [] # list of all prime numbers

    for j in range(2,1000000):
        # if not crossed out, then it is prime
        if listP[j] == 1:
            primes.append(j)
            mul = 2
            while mul*j < 1000000:
                if mul*j == 179:
                    print mul
                    print j
                listP[mul*j] = 0
                mul += 1
    i = 3
    count = 1
    cir= []
    while i < 1000000:
        if listP[i] == 1 and allDigitsOdd(i) and circularPrime(i, listP):
            count += 1
            cir.append(i)
        i += 2
    return count

def allDigitsOdd(n):
    while n != 0:
        digit = n%10
        if digit%2 == 0:
            return False
        n /= 10
    return True

def circularPrime(n,listPrimes):
    rotations = allRotations(n)
    for rot in rotations:
        # if rot is not prime, return false
        if listPrimes[listToNum(rot)] == 0:
            return False
    return True

def allRotations(n):
    listOfLists = [numToList(n)]
    for i in range(len(li)-1):
        first = li[0]
        del li[0]
        li.insert(len(li)-1, first)
        copy = li[:]
        listOfLists.append(copy)
    return listOfLists

"""
PROBLEM 36

The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""
def prob36():
    sumSoFar = 0
    for i in range(1,1000000):
        if isPalin(i) and isPalin(toBinary(i)):
            sumSoFar += i
    return sumSoFar


def toBinary(n):
    binaryli = []
    while n != 0:
        diff = n%2
        binaryli.append(diff)
        n -= diff
        n /= 2
    binaryli.reverse()
    return listToNum(binaryli)


"""
PROBLEM 37

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits
from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def prob37():
    truncprimes = []
    sumSoFar = 0
    primesActive = [3,7,9]
    odds = [1,2,3,5,7,9]
    base = [3,7,9]
    i = 33
    """
    while len(truncprimes) != 11:
        if isTruncPrime(i):
            truncprimes.append(i)
        sumSoFar += i
        i += 2
    """
    for prime in primesActive:
        findTruncPrime(prime,truncprimes,odds)
    print truncprimes
    return sum(truncprimes)


def findTruncPrime(n,truncprimes,odds):
    if not isPrime(n):
        return
    li = numToList(n)
    for new in odds:
        licopy = li[:]
        licopy.insert(0,new)
        num = listToNum(licopy)
        if isPrime(num):
            if isPrimeRightLeft(licopy):
                truncprimes.append(num)
            if new != 2 and new != 5:
                findTruncPrime(num,truncprimes,odds)


def isPrimeRightLeft(li):
    while li:
        curr = listToNum(li)
        if not isPrime(curr):
            return False
        li.pop()
    return True

"""
PROBLEM 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital,
192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be
formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
def prob38():
    maxSoFar = 918273645
    for i in range(90,10000):
        if numToList(i)[0] < 9:
            continue
        n = 1
        while n < 5:
            contProd = concatenatedProduct(i,n)
            if len(contProd) > 9:
                break
            elif listToNum(contProd) > maxSoFar and isPandigital(contProd):
                maxSoFar = listToNum(contProd)
            n += 1
    return maxSoFar




def concatenatedProduct(num,listTo):
    li = []
    for i in range(1,listTo+1):
        li.extend(numToList(num*i))
    return li

def isPandigital(digitsList):
    if len(digitsList) != 9:
        return False
    digits = set(range(1,10))
    currDigits = set(digitsList)
    diff = digits - currDigits
    return not diff # if diff is empty, return true

"""
PROBLEM 39

If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

def prob39():
    maxSols = 3
    tripleDict = dict((i,0) for i in range(1,1001))
    m = 2
    n = 1
    while m<30:
        while n<m:
            if ((m-n)%2 == 1 and gcd(n,m) == 1):
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                sumP = a+b+c
                k = 1
                while sumP*k <= 1000:
                    tripleDict[sumP*k] += 1
                    k += 1
            n += 1
        n = 1
        m+=1
    maxSoFar = 0
    for i in tripleDict.keys():
        if tripleDict[i] > maxSols:
            maxSoFar = i
            maxSols = tripleDict[i]
    return maxSoFar



