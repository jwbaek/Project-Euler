
# probably the worst 'isPrime' function ever..
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# given 1234, returns [1,2,3,4]
def numToList(n):
    return [int(s) for s in str(n)]

# given [1,2,3,4] return 1234
def listToNum(li):
    num = 0
    for i in li:
        num *= 10
        num += i
    return num

def isPalin(n):
    li = []
    while n != 0:
        li.append(n%10)
        n /= 10
    for i in range(len(li)/2):
        if(li[i] != li[len(li)-i-1]):
            return False
    return True

def gcd(num1,num2):
    a = num1
    b = num2
    while (a != 0):
        temp = a
        a = b%a
        b = temp
    return b

# returns set of all primes less than largest
def prime_sieve(largest):
    # listP is 1 if prime
    listP = [1] * (largest+1)
    listP[0] = 0
    listP[1] = 0
    prime = set([]) # list of all prime numbers

    for j in range(2,largest):
        # if not crossed out, then it is prime
        if listP[j] == 1:
            prime.add(j)
            mul = 1
            while mul*j < largest:
                listP[mul*j] = 0
                mul += 1
    return prime

def toBinary(n):
    binaryli = []
    while n != 0:
        diff = n%2
        binaryli.append(diff)
        n -= diff
        n /= 2
    binaryli.reverse()
    return listToNum(binaryli)