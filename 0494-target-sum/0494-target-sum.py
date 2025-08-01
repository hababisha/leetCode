class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, tot):
            if i == len(nums):
                return 1 if tot == target else 0
            
            if (i, tot) not in memo:
                add = dp(i+1, tot +nums[i])
                sub = dp(i+1, tot - nums[i])
                memo[(i,tot)] = add+sub
            return memo[(i,tot)]
        return dp(0,0)