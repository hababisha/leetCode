class Solution:
    def fib(self, n: int) -> int:
        def dp(n):
            if n < 2: return n
            if n in cache: return cache[n]

            cache[n] = self.fib(n-2) + self.fib(n-1)
            return cache[n]
        
        cache = {}
        return dp(n)