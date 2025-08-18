class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        n = bin(n)[2:]

        for i in n:
            if i == "1":
                ans += 1
        return ans