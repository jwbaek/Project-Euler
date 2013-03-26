import itertools
from decimal import *
from Common_Functions import *
"""
PROBLEM 60

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime.

For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

max_prime_60 = 9000
primes_60 = prime_sieve(max_prime_60)

def add_to_dict(p1, p2, concat_primes_dict):
    if p1 not in concat_primes_dict:
        concat_primes_dict[p1]= [p2]
    else:
        flag = True
        for old_prime in concat_primes_dict[p1]:
            if not has_remarkable_property((old_prime, p2)):
                flag = False
                break
        if flag:
            concat_primes_dict[p1].append(p2)

def prob60():
    concat_primes_dict = {}
    for prime_set in itertools.combinations(primes_60, 2):
        if has_remarkable_property(prime_set):
            add_to_dict(prime_set[0], prime_set[1], concat_primes_dict)
            add_to_dict(prime_set[1], prime_set[0], concat_primes_dict)
    possible_sols = []
    # find all primes that have 4 or more concat_primes
    for (k, v) in concat_primes_dict.iteritems():
        if len(v) >= 4:
            v.append(k)
            possible_sols.append(v)
    if not possible_sols:
        print 'NONE FOUND FOR', max_prime_60
        return
    # find the minimum of all possible solutions
    minimum = sum(possible_sols[0])
    for prime_set in possible_sols:
        for tuple5 in itertools.combinations(prime_set, 5):
            sum_primes = sum(tuple5)
            if sum_primes < minimum:
                minimum = sum_primes
            if sum_primes == 103:
                print tuple5
    return minimum

def has_remarkable_property(prime_set):
    for tup in itertools.permutations(prime_set, 2):
        concat = concat_nums(tup[0], tup[1])
        if concat >= max_prime_60:
            if not isPrime(concat):
                return False
        elif concat not in primes_60:
            return False
    return True

def concat_nums(num1, num2):
    return int(str(num1) + str(num2))


"""
PROBLEM 61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	    P4,n=n^2	 	    1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n-1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n-3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n-2)	 	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281,
has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first
two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281),
and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers
for which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the set.
"""
import math

# I should have probably just created a list of all of these numbers
# that are four digits, insead of creating a is<n-gonal> function for each number
def isTriangular(n):
    x = (math.sqrt(8*n + 1) - 1 )/2
    if math.floor(x) == x:
        return x
    return False
def isSquare(n):
    x = (math.sqrt(n))
    if math.floor(x) == x:
        return x
    return False
def isHexagonal(n):
    x = (math.sqrt(8*n + 1) + 1 )/4
    if math.floor(x) == x:
        return x
    return False
def isHeptagonal(n):
    x = (math.sqrt(40*n + 9) + 3 )/10
    if math.floor(x) == x:
        return x
    return False
def isOctagonal(n):
    x = (math.sqrt(12*n + 4) + 2 )/6
    if math.floor(x) == x:
        return x
    return False

def isPentagonal(n):
    x = (math.sqrt(24*n + 1) + 1 )/6
    if math.floor(x) == x:
        return x
    return False

def octagonal(n):
    return n*(3*n-2)

def prob61():
    n = 19
    left = [3, 4, 5, 6, 7]
    for n in range(19, 60):
        list_so_far = [octagonal(n)]
        first = octagonal(n)
        found = find_all_sets(list_so_far, left)
        if found:
            return found, sum(found)

func_dict = {3:isTriangular, 4:isSquare, 5:isPentagonal, 6:isHexagonal, 7:isHeptagonal, 8:isOctagonal}
def list_startswith(number, startswith, endswith=False):
    func = func_dict[number]
    li= []
    found = -1
    for n in xrange(startswith*100, startswith*100+100):
        if tensdigit(n) != 0 and func(n):
            if endswith:
                if n%100 == endswith:
                    li.append(n)
            else:
                li.append(n)
            found = func(n)
    return li

def tensdigit(n):
    return n/10%10

def find_all_sets(so_far, left):
    if not left:
        return so_far
    li_tuples = []
    endswith = False
    if len(left) == 1:
        endswith = so_far[0]/100
    for i in left:
        li= list_startswith(i, so_far[-1]%100, endswith = endswith)
        if li:
            for new in li:
                local_so_far = so_far[:]
                local_so_far.append(new)
                local_left = left[:]
                local_left.remove(i)
                li_tuples.append((local_so_far, local_left))
    for (sofar, whatsleft) in li_tuples:
        result = find_all_sets(sofar, whatsleft)
        if result:
            return result
    return False

"""
PROBLEM 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
def prob62():
    length = 12
    sorted_dict = {} # sorted str: (count, min_value)
    cubes = [n**3 for n in xrange(10000) if has_ndigits(n**3,length)]
    for num in cubes:
        sorted_str = "".join(sorted(str(num)))
        # if key already exists
        if sorted_str in sorted_dict:
            sorted_dict[sorted_str][0] += 1
            if num < sorted_dict[sorted_str][1]:
                sorted_dict[sorted_str][1] = num
        else:
            sorted_dict[sorted_str] = [1, num]
    minimum = 10**13
    # find min
    for (k, v) in sorted_dict.iteritems():
        if v[0] == 5 and v[1] < minimum:
            minimum = v[1]
    return minimum


def is_permutation(n1, n2):
    str1 = str(n1)
    str2= str(n2)
    if len(str1) == len(str2):
        return sorted(str(n1)) == sorted(str(n2))
    return 0

def has_ndigits(num, digits):
    res = num/10**(digits-1)
    return res != 0 and res < 10

"""
PROBLEM 63

The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

def prob63():
    count = 0
    for n in range(1,10):
        exp = 1
        digits_power = 1
        while digits_power >= exp-1:
            power = n**exp
            digits_power = num_digits(power)
            if exp == digits_power:
                count += 1
            exp += 1
    return count

def num_digits(n):
    return len(str(n))

"""
PROBLEM 69

Euler's Totient function, ?(n) [sometimes called the phi function],
is used to determine the number of numbers less than n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, ?(9)=6.

n	Relatively Prime	?(n)	  n/?(n)
2	1	                  1	        2
3	1,2	                  2	        1.5
4	1,3	                  2       	2
5	1,2,3,4	              4	        1.25
6	1,5	                  2	        3
7	1,2,3,4,5,6	          6	        1.1666...
8	1,3,5,7	              4	        2
9	1,2,4,5,7,8	          6	        1.5
10	1,3,7,9	              4      	2.5
It can be seen that n=6 produces a maximum n/?(n) for n <= 10.

Find the value of n  1,000,000 for which n/?(n) is a maximum.
"""
def prob69():
    max_num = 1000000
    d = relative_primes_dict(max_num)
    max_totient = 3
    number = 6
    for i in range(2,max_num):
        curr_totient = totient(i, d[i])
        if max_totient < curr_totient:
            max_totient = curr_totient
            number = i
            print number
    return number, max_totient

def relative_primes_dict(largest=1000000):
    d = dict((i, 1) for i in range(largest))
    listP = [1] * (largest+1)
    listP[0] = 0
    listP[1] = 0
    prime = [] # list of all prime numbers
    for j in range(2, largest):
        if listP[j] == 1:
            prime.append(j)
            mul = 1
            while mul*j < largest:
                listP[mul*j] = 0
                d[mul*j] += mul - 1
                mul += 1
    return d

def totient(n, relative_primes):
    count = n - relative_primes
    if count == 0:
        print n
    return Decimal(n)/Decimal(count)


"""
PROBLEM 97
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 269725931; it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes, of the form 2p1, have been found which contain
more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
 2,357,207 digits: 2^843327830457+1.

Find the last ten digits of this prime number.
"""

def prob97():
    i = 0
    curr = 2
    while i < 843327830457:
        curr *= 2
        curr%(10**10)
        i += 1
    return curr+1



