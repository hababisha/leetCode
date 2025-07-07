class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        curS = 0
        for i in range(len(nums)):
            curS += nums[i]
            ans = max(ans, curS)
            if curS < 0:
                curS = 0 
        return ans

