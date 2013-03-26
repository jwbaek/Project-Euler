#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jackie
#
# Created:     28/12/2012
# Copyright:   (c) Jackie 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Common_Functions import *

"""
PROBLEM 1

If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5
below 1000.
"""

def prob1():
    sum1 = 0

    # add up multiples of 3
    sum1 += 333*(3+999)/2
    # 166833

    # add up multiples of 5
    sum1 += 199*(5+995)/2

    # subtract multiples of 15
    sum1 -= 66*(15+990)/2
    return sum1



"""
PROBLEM 2

Each new term in the Fibonacci sequence is generated
by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million,
find the sum of the even-valued terms.
"""

def prob2():
    fib1 = 1
    fib2 = 2
    sum2 = 0
    while (fib2 <= 4000000):
        if (fib2%2 == 0):
            sum2 += fib2
        temp = fib1
        fib1 = fib2
        fib2 += temp
    return sum2



"""
PROBLEM 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the
number 600851475143 ?
"""

# Sieve of Eratosthenes
def prob3():
    largest = 600851475143
    # listP is 1 if prime
    listP = [1] * 1000000
    listP[0] = 0
    listP[1] = 0
    prime = []

    for j in range(2,1000000):
        # if not crossed out
        if listP[j] == 1:
            prime.append(j)
            mul = 1
            while mul*j < 1000000:
                listP[mul*j] = 0
                mul += 1

    k = len(prime) -1
    while k >= 0:
        if 600851475143 % prime[k] == 0:
            return prime[k]
        k -= 1

"""
easier solution:

def prob3():
    i = 1000000
    while i > 0:
        if 600851475143%i == 0 and isPrime(i):
            return i
        i -= 1
"""

"""
PROBLEM 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product
of two 3-digit numbers.
"""
def isPalin(n):
    li = []
    while n != 0:
        li.append(n%10)
        n /= 10
    for i in range(len(li)/2):
        if(li[i] != li[len(li)-i-1]):
            return False
    return True

def prob4():
    num1 = 999
    num2 = 999
    largest = 0
    while num1 >= 100:
        while num2 >= 100:
            prod = num1*num2
            if isPalin(prod) and prod >= largest:
                largest = prod

            num2 -= 1
        num2 = 999
        num1 -= 1
    return largest

"""
PROBLEM 5

2520 is the smallest number that can be
divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number
that is evenly divisible by all of the numbers
 from 1 to 20?
"""
def gcf(num1,num2):
    a = num1
    b = num2
    while (a != 0):
        temp = a
        a = b%a
        b = temp
    return b

def lcm(a,b):
    gcfs = gcf(a,b)
    return a/gcfs * b

def prob5():
    soFar = lcm(1,2)
    for i in range(3, 21):
        soFar = lcm(soFar,i)
    return soFar

"""
PROBLEM 6

The sum of the squares of the first
 ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten
 natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the
sum of the squares of the first ten
natural numbers and the square of the sum
 is 3025  385 = 2640.

Find the difference between the
sum of the squares of the first
one hundred natural numbers and the
square of the sum.
"""
def prob6():
    sumOfSquares = 0
    squareOfSum = (1+100)*100/2
    squareOfSum *= squareOfSum
    for i in range(1,101):
        sumOfSquares += i*i
    return squareOfSum - sumOfSquares

"""
PROBLEM 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
# returns true if n is prime, given a list of all prime numbers smaller than n
def isPrime(n,listPrimes):
    for prime in listPrimes:
        if n%prime == 0:
            return False
    return True

def prob7():
    liPrimes = [2]
    curr = 3
    while (len(liPrimes) != 10001):
        if (isPrime(curr,liPrimes)):
            liPrimes.append(curr)
        curr += 1
    return liPrimes[10000]

"""
PROBLEM 8

Find the greatest product of five consecutive digits in the 1000-digit number.

7316717653133062491922511967442657474235534919493496983520312
77450632623957831801698480186947885184385861560789112949495459
50173795833195285320880551112540698747158523863050715693290963
29522744304355766896648950445244523161731856403098711121722383
11362229893423380308135336276614282806444486645238749303589072
96290491560440772390713810515859307960866701724271218839987979
08792274921901699720888093776657273330010533678812202354218097
51254540594752243525849077116705560136048395864467063244157221
55397536978179778461740649551492908625693219784686224828397224
13756570560574902614079729686524145351004748216637048440319989
00088952434506585412275886668811642717147992444292823086346567
48139191231628245861786645835912456652947654568284891288314260
76900422421902267105562632111110937054421750694165896040807198
40385096245544436298123098787992724428490918884580156166097919
13387549920052406368991256071760605886116467109405077541002256
98315520005593572972571636269561882670428252483600823257530420
752963450

"""
def turnIntoList(n):
    li = []
    while n != 0:
        li.append(n%10)
        n /= 10
    return li

# calculate product of five numbers in li, starting at pos
def prodFive(li, pos):
    return li[pos]*li[pos+1]*li[pos+2]*li[pos+3]*li[pos+4]

def prob8(n):
    li = turnIntoList(n)
    curr = 0
    largestProd = 0
    while curr < 996:
        currProd = prodFive(li,curr)
        if (prodFive(li,curr) > largestProd):
            largestProd = currProd
        if (curr+5 >= 996):
            break
        # if next is 0, then push curr all the way until first non-zero
        if (li[curr+5] == 0):
            k = 6
            while (curr+k < 996 and [curr+k] == 0):
                k+=1
            curr += k
        else:
            curr += 1
    return largestProd

"""
PROBLEM 9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
def gcd(num1,num2):
    a = num1
    b = num2
    while (a != 0):
        temp = a
        a = b%a
        b = temp
    return b

def prob9():
    m = 2
    n = 1
    while m<30:
        while n<m:
            if ((m-n)%2 == 1 and gcd(n,m) == 1):
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                sumP = a+b+c
                k = 1000/sumP
                if (k * sumP) == 1000:
                    print a*k
                    print b*k
                    print c*k
                    return
            n += 1
        n = 1
        m+=1


"""
PROBLEM 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
# Sieve of Eratosthenes
def prob10():
    largest = 2000000
    # listP is 1 if prime
    listP = [1] * 2000000
    listP[0] = 0
    listP[1] = 0
    prime = [] # list of all prime numbers

    for j in range(2,2000000):
        # if not crossed out, then it is prime
        if listP[j] == 1:
            prime.append(j)
            mul = 1
            while mul*j < 2000000:
                listP[mul*j] = 0
                mul += 1
    # now sum up all numbers in prime
    sumPrimes = 0
    k = len(prime) -1
    while k >= 0:
        sumPrimes += prime[k]
        k -= 1
    return sumPrimes

















