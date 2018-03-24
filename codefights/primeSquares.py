import math
def primeSquare(n):
    isprimes = primes(n+1)
    
    if isprimes[n]:
        return n ** 2
    s = 0
    for i in range(1, n+1):
        if isprimes[i]:
            s += (i ** 2)
        else:
            s += i
    return s
def primes(n):
    isprimes = [True] * max(n, 2)
    isprimes[0], isprimes[1] = False, False
    x = 2
    while x < math.sqrt(n):
        if isprimes[x]:
            p = x * x
            while p < n:
                isprimes[p] = False
                p += x
                
        x += 1
    return isprimes
print primeSquare(4)
