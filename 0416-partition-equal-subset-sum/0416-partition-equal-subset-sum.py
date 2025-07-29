class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2:
            return False
        half = summ // 2
        
        def dp(i, sofar):
            if i == len(nums):
                if sofar == half:
                    return True
                return False
            
            if (i, sofar) not in memo:
                memo[(i, sofar)] = dp(i+1, sofar+nums[i]) or dp(i+1, sofar)
            return memo[(i, sofar)]
        
        memo = {}
        return dp(0, 0)