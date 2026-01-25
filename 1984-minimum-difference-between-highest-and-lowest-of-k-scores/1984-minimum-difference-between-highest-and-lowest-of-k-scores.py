class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if k > len(nums)-1: return nums[-1] - nums[0]
        ans = nums[k-1]-nums[0]
        l = 1
        for r in range(k, len(nums)):
            ans = min(ans, nums[r] - nums[l])
            l += 1
        return ans

        1, 4, 7, 9