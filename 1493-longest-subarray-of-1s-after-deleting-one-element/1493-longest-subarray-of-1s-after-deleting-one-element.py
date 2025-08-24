class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        l = 0
        maxxCount = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
            maxxCount = max(maxxCount, r-l+1)
        return maxxCount - 1