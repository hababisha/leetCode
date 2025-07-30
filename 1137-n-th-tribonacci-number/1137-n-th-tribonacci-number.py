class Solution:
    def tribonacci(self, n: int) -> int:
        def trib(n):
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1
            if n not in memo:
                memo[n] = trib(n-3) + trib(n-2) + trib(n-1)
            return memo[n]
        
        memo ={}
        return trib(n)