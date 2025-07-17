class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0, len(nums) -1
        ans = 0
        while l < r:
            summ = nums[l] + nums[r]
            ans = max(summ,ans)
            l +=1
            r -= 1
        return ans