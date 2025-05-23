class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        res = 0
      
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                res = max(res, j - i)
        return res
