class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        lastNum = 1
        count = 0
        index = 0
        while n >= lastNum:
            if index < len(nums) and nums[index] <= lastNum:
                lastNum += nums[index]
                index += 1
            else:
                count += 1
                lastNum += lastNum
        return count