import math
def CountProgram(length):
    if length < 2:
        return 6
    if length == 2:
        return pow(6,2) + 1
    
    ans = 0
    for i in range(0, length, 2):
        # i = num of brackets
        if i:
            ans += pow(6, length - i) * n_choose_k(length, i)
        else:
            ans += pow(6, length - i)
        #print "i: ", i, " ans: ", ans, " n_choose_k(i, 2): ", n_choose_k(i, 2)
        #ans += n_choose_k(i, 2)
    print ans
    return ans % (pow(10, 9) + 7) 

def n_choose_k(n, k):
    '''
    if k == 0:
        return 1
    if k == n:
        return 1
    return n_choose_k(n-1, k-1) + n_choose_k(n-1, k)
    '''
    if k > n / 2:
        k = n - k

    result = 1.0

    for i in range(1,k+1):
        result *= ((n - (k - i)) / float(i))

    return int(result)

def catalan(n):
    c = n_choose_k(2*n, n)
    return c/(n+1)

print CountProgram(15)
