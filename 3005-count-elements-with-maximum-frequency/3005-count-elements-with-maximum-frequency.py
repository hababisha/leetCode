class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = Counter(nums)
        mx = max(m.values())
        res = 0
        for v in m.values():
            if v == mx:
                res += mx
        return res