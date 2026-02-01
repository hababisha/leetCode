class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        s = sorted(nums[1:])
        return ans + s[0] + s[1]