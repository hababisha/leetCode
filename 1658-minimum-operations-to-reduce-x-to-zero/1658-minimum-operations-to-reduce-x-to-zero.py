class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        summ = sum(nums)
        target = summ - x
        l = 0
        curSum = 0
        maxL = -1
        for r in range(len(nums)):
            curSum += nums[r]

            while l <= r and curSum > target:
                curSum -= nums[l]
                l += 1
            
            if curSum == target:
                maxL = max(maxL, r-l+1)
        return -1 if maxL == -1 else len(nums) - maxL
