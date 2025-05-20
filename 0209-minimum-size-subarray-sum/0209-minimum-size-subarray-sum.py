class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minL = float("inf")
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                minL = min(minL, r-l+1)
                summ -= nums[l]
                l += 1
        return minL if minL < float('inf') else 0

