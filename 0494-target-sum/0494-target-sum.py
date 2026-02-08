class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i,tar):
            if i == len(nums):
                return 1 if tar == 0 else 0
            
            if (i,tar) not in memo:
                memo[(i,tar)] = dp(i+1, tar+nums[i]) + dp(i+1, tar-nums[i])
            return memo[(i,tar)]
        return dp(0, target)