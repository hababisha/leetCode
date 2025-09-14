class Solution:
    def smallestValue(self, n: int) -> int:
        def primes(n):
            res = 0
            for i in range(2, int(n**0.5)+1):
                while n % i == 0:
                    res += i
                    n //= i
            if n >= 2:
                res += n
            return res
        
        while n != primes(n):
            n = primes(n)
        return n
