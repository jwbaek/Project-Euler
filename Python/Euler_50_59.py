#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jackie
#
# Created:     09/03/2013
# Copyright:   (c) Jackie 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Common_Functions import *
"""
PROBLEM 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the
sum of the most consecutive primes?
"""

def prob50():
    primes = prime_sieve(1000000)
    liprimes = list(primes)
    liprimes.sort()
    longestlength = 21
    longest = 953
    curr = 3
    for i in range(3,4704):
        length = longestlength + 2
        sumseq = sum(liprimes[i:i+length])
        while sumseq < 1000000:
            if sumseq in primes:
                longestlength = length
                longest= sumseq
            length += 2
            sumseq = sum(liprimes[i:i+length])
    return longest


"""
PROBLEM 51

By replacing the 1st digit of *3,
it turns out that six of the nine possible values:
    13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
    56003, 56113, 56333, 56443, 56663, 56773, and 56993.
    Consequently 56003, being the first member of this family,
     is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""
import string
def prob51(digits):
    primesUpper = prime_sieve(10**(digits + 1))
    primesLower = prime_sieve(10**digits)
    primes = primesUpper - primesLower
    sortedprimes = list(primes)
    sortedprimes.sort()
    for p in sortedprimes:
        unique_digits = set(numToList(p))
        for d in unique_digits:
            count = 0
            for i in range(10):
                newNum = int(string.replace(str(p), str(d), str(i)))
                if newNum in primes:
                    count += 1
            if count == 8:
                return p, d

def replace_digits(num, pos, toreplace):
    li = numToList(num)


"""
PROBLEM 52

It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x,
such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def prob52():
    digits = 1
    while True:
        curr = 10**(digits-1)
        while 6*curr < 10**(digits):
            if digitsEqual(curr, 2*curr) and digitsEqual(curr, 3*curr) and digitsEqual(curr, 4*curr) and digitsEqual(curr, 5*curr) and digitsEqual(curr, 6*curr):
                return curr
            curr += 1
        digits += 1




def digitsEqual(num1, num2):
    return set(numToList(num1)) == set(numToList(num2))

"""
PROBLEM 53

nCr =
n!
r!(nr)!
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
"""

def prob53():
    count = 0
    n = 23
    while n <= 100:
        for r in range(n/2+1):
            curr = nCr(n, r)
            if curr > 1000000:
                half = n/2 + 1
                count += (half - r)*2
                if n%2 == 0:
                    count -= 1
                break
        n += 1
    return count

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

from operator import mul    # or mul=lambda x,y:x*y

def nCk(n,k):
    return int(round(reduce(mul, (float(n-i)/(i+1) for i in range(k)), 1)))

"""
PROBLEM 54

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
    the first five are Player 1's cards and the last five are Player 2's cards.
    You can assume that all hands are valid (no invalid characters or repeated cards),
    each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
"""
High Card: 1
One Pair: 2
Two Pairs: 3
Three of a Kind: 4
Straight: 5
Flush: 6
Full House: 7
Four of a Kind: 8
Straight Flush: 9
Royal Flush: 10
"""

# this question was just too long..
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def prob54():
    f = open("C:\Users\Jackie\Documents\Project Euler\Python\prob54.txt", "r")
    count1 = 0
    count2 = 0
    for line in f:
        line = line.split()
        hand1 = gethand(line[:5])
        hand2 = gethand(line[5:])
        if firstPlayerWin(sortHand(hand1), sortHand(hand2)):
            count1 += 1
        else:
            count2 += 1
    return count1

# return True if hand1 won
def firstPlayerWin(hand1, hand2):
    rank1 = determineHandRank(hand1)
    rank2 = determineHandRank(hand2)
    print rank1, rank2
    if rank1 == rank2:
        return determineTie(hand1, hand2, rank1)
    return rank1 > rank2

# return True if hand1 won
def determineTie(hand1, hand2, rank):
    # high card
    if rank == 1:
        for i in range(4,-1,-1):
            if hand1[i].rank != hand2[i].rank:
                return hand1[i].rank > hand2[i].rank
    if rank == 2:
        return determineWinnerSame(hand1, hand2, 2)
    if rank == 3:
        firstPair1 = getSame(hand1, 2)
        firstPair2 = getSame(hand2, 2)
        removeRank(hand1, firstPair1)
        removeRank(hand2, firstPair2)
        secondPair1 =getSame(hand1, 2)
        secondPair2 =getSame(hand2, 2)
        if secondPair1 != secondPair1:
            return secondPair1 > secondPair2
        if firstPair1 != firstPair2:
            return firstPair1 > secondPair2
        removeRank(hand1, secondPair1)
        removeRank(hand2, secondPair2)
        return hand1[0].rank > hand2[0].rank
    # three of a kind
    if rank == 4:
        return determineWinnerSame(hand1, hand2, 3)
    # straight
    if rank == 5:
        return determineWinnerStraight(hand1, hand2)
    # flush
    if rank == 6:
        for i in range(4, -1, -1):
            if hand1[i].rank != hand2[i].rank:
                return hand1[i].rank > hand2[i].rank
    # full house
    if rank == 7:
        triple1 = getSame(hand1, 3)
        triple2 = getSame(hand2, 3)
        return triple1 > triple2
    # four of a kind
    if rank == 8:
        return determineWinnerSame(hand1, hand2, 4)
    # straight flush
    if rank == 9:
        return hand1[0].rank > hand2[0].rank

def printHand(hand):
    for card in hand:
        print card.rank, card.suit

# returns the rank of the card
def getSame(hand, num):
    count = 1
    prev = hand[0].rank
    for i in range(1, len(hand)):
        if hand[i].rank == prev:
            count += 1
        else:
            prev = hand[i].rank
            count = 1
        if count == num:
            return prev
    return -1

def removeRank(hand, rank):
    copy = hand[:]
    for card in copy:
        if card.rank == rank:
            hand.remove(card)


def determineWinnerSame(hand1, hand2, num):
    same1 = getSame(hand1, num)
    same2 = getSame(hand2, num)
    if same1 == same2:
        removeRank(hand1, same1)
        removeRank(hand2, same2)
        printHand(hand1)
        printHand(hand2)
        for i in range(len(hand1)-1, -1, -1):
            if hand1[i].rank != hand2[i].rank:
                return hand1[i].rank > hand2[i].rank
        return -1
    else:
        return same1 > same2

def determineWinnerStraight(hand1, hand2):
    if hand1[0].rank == 2 and hand1[4].rank == 14:
        return False
    if hand2[0].rank == 2 and hand2[4].rank == 14:
        return True
    return hand1[0].rank > hand2[0].rank

def determineHandRank(hand):
    flush = isFlush(hand)
    if flush:
        if isRoyalStraight(hand):
            return 10
        if isStraight(hand):
            return 9
    same = sameRank(hand)
    if same:
        if same[0] == 4:
            return 8
        if same == [2,3] or same == [3,2]:
            return 7
    if flush:
        return 6
    if isStraight(hand):
        return 5
    if same:
        if same[0] == 3:
            return 4
        if same == [2,2]:
            return 3
        else:
            return 2
    return 1

def printHand(hand):
    for card in hand:
        print card.rank, card.suit

def gethand(line):
    hand = []
    for word in line:
        hand.append(Card(word[1], toInt(word[0])))
    return hand

def toInt(rank):
    if rank == 'T':
        return 10
    if rank == 'J':
        return 11
    if rank == 'Q':
        return 12
    if rank == 'K':
        return 13
    if rank == 'A':
        return 14
    return int(rank)


def sortHand(hand):
    return sorted(hand, key = lambda(card): card.rank)

def isFlush(hand):
    for i in range(4):
        if hand[i].suit != hand[i+1].suit:
            return False
    return True

# true if straight is 10 to Ace
def isRoyalStraight(hand):
    if hand[0].rank == 10 and hand[1].rank == 11 and hand[2].rank == 12 and hand[3].rank == 13 and hand[4].rank == 14:
        return True

# true if straight (but false if royal straight)
def isStraight(hand):
    if isRoyalStraight(hand):
        return True
    length = 4
    if hand[4].rank == 14 and hand[0].rank == 2:
        length = 3
    for i in range(length):
        if hand[i].rank+1 != hand[i+1].rank:
            return False
    return True

# return list of all same ranks
# ie. [2] for a pair, [2,2] for two pair, [2,3] for full house
def sameRank(hand):
    same = []
    i = 0
    while i <= 3:
        count = 1
        if hand[i].rank == hand[i+1].rank:
            j = i+1
            count += 1
            while j+1 <= 4:
                if hand[j].rank == hand[j+1].rank:
                    count += 1
                else:
                    break
                j += 1
            same.append(count)
        i+=count
    return same

"""
PROBLEM 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and
add process is called a Lychrel number.
You are given that for every number below ten-thousand, it will either
(i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists,
has managed so far to map it to a palindrome.

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""

def prob55():
    count = 0
    nonLychrel = set([])
    for i in range(10,10001):
        if isLychrel(i, nonLychrel):
            count += 1
    return count

def isLychrel(n, nonLychrel):
    n += reverse(n)
    if n in nonLychrel:
        return False
    for i in range(50):
        if isPalindrome(n):
            nonLychrel.add(n)
            return False
        n += reverse(n)
    return True

def isPalindrome(n):
    li = []
    while n != 0:
        li.append(n%10)
        n /= 10
    for i in range(len(li)/2):
        if(li[i] != li[len(li)-i-1]):
            return False
    return True

def reverse(n):
    rev = 0
    while n != 0:
        rev *= 10
        digit = n%10
        rev += digit
        n /= 10
    return rev

"""
PROBLEM 56

A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?
"""

def prob56():
    maxSoFar = 1
    for a in range(1, 101):
        for b in range(1,101):
            currSum = digital_sum(a**b)
            if currSum > maxSoFar:
                maxSoFar = currSum
    return maxSoFar

def digital_sum(n):
    li = list(str(n))
    return reduce(sum_string, li, 0)

def sum_string(accum_value, x):
    return accum_value + int(x)

"""
PROBLEM 57

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

 sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator
exceeds the number of digits in the denominator.

In the first one-thousand expansions,
how many fractions contain a numerator with more digits than denominator?
"""

def prob57():
    count = 0
    currFrac = (1, 2)
    for i in range(1000):
        numerator = currFrac[1]
        denominator = currFrac[0] + 2*currFrac[1]
        currFrac =(numerator, denominator)
        total = reduceFrac((numerator + denominator, denominator))
        if len(str(total[0])) > len(str(total[1])):
            count += 1
    return count

def reduceFrac(frac):
    g = gcd(frac[0], frac[1])
    return (frac[0]/g, frac[1]/g)

"""
PROBLEM 58

Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along
the bottom right diagonal, but what is more interesting is that 8 out of the 13
numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral
for which the ratio of primes along both diagonals first falls below 10%?
"""
def prob58():
    lenprimes = 8
    lentotal = 13
    i = 4
    while lenprimes*10 >= lentotal:
        lenprimes += num_newprimes_spiral(i)
        lentotal += 4
        i += 1
    return (i-1)*2+1


def num_newprimes_spiral(n):
    bottom_right = (n*2+1)**2
    li = []
    for i in range(1,4):
        li.append(bottom_right-2*n*i)
    count = 0
    for num in li:
        if isPrime(num):
            count += 1
    return count





