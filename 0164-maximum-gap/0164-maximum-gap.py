class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxx = 0
        if len(nums) < 2:
            return 0
        
        nums.sort()
        
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i-1]
            maxx = max(gap, maxx)

        return maxx