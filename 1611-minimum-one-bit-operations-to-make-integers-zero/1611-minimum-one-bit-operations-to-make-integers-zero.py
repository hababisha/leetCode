class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        sign = 1
        ans = 0
        for i in range(32, -1,-1):
            if n & (1 << i):
                ans += sign * ((1 << (i+1)) -1)
                sign *= -1
        return ans

