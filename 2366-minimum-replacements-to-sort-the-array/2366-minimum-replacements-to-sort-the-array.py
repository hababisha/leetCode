class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        lim = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            left = nums[i]
            if left > lim:
                parts = math.ceil(left/lim)
                res += parts - 1
                lim = left //parts
            else:
                lim = left
        return res