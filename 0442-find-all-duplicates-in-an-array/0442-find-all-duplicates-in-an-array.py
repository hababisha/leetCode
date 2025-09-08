class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        m = {}
        ans = []
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        for v in m:
            if m[v] == 2:
                ans.append(v)
        return ans