class Solution:
    def rob(self, nums: List[int]) -> int:
        l = 0
        r = 1
        su = 0
        su2 = 0
        while r <= len(nums) - 1:
            su += nums[r]
            r += 2
        while l<= len(nums) -1:
            su2 += nums[l]
            l += 2
        return max(su, su2)

       