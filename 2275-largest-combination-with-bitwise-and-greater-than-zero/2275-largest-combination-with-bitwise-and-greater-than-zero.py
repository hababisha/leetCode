class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32, -1, -1):
            c = 0   
            for n in candidates:
                if (n & (1 << i)):
                    c += 1
            ans = max(ans, c)
        return ans
        
