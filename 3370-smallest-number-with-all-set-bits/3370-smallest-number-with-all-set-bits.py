class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return 1

        for i in range(n, 10000000):
            if i-1 < n:
                continue
            if i & (i-1) == 0:
                return i-1