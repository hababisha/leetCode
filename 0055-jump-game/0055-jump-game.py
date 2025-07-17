class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastgoodidxpos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastgoodidxpos:
                lastgoodidxpos = i
        return lastgoodidxpos == 0