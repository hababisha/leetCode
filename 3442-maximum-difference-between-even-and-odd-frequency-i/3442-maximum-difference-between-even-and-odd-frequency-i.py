class Solution:
    def maxDifference(self, s: str) -> int:
        m = Counter(s)
        maxO, minE = 0, float(inf)

        for val in m:
            if m[val] % 2:
                maxO = max(maxO, m[val])
            else:
                minE = min(minE, m[val])
        
        return maxO - minE