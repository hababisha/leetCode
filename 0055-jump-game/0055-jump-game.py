class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lgi = len(nums) - 1
        for i in range(len(nums)-1, -1,-1):
            if nums[i] + i >= lgi:
                lgi = i
        return lgi == 0