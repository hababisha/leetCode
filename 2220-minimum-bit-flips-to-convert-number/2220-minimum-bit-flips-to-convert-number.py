class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        check = start ^ goal
        ans = 0
        for i in range(32):
            if check & (1<<i): ans += 1
        return ans