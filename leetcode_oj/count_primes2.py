class  Solution : 
    #param {Integer} N 
    #return {Integer} 
    def  countPrimes (self, N) : 
        isPrime = [ True ] * max (N, 2 )
        isPrime [ 0 ], isPrime [ 1 ] = False , False 
        x = 2 
        while x * x < N:
			if isPrime [x]:
				p = x * x
				while p < N:
					isPrime[p] = False
					p += x
			x += 1
        return sum(isPrime)

s = Solution()
print s.countPrimes(15)
