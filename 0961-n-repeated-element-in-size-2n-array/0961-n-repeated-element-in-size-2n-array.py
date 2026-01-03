class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = Counter(nums)
        for k,v in m.items():
            if v == len(nums)//2:
                return k