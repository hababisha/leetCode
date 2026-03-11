
class Solution:
    def longestEqualSubarray(self, nums, k):
        l = 0
        m = defaultdict(int)
        ans = 0
        res = 0
        for r in range(len(nums)):
            m[nums[r]] += 1

            res  = max(res, m[nums[r]])
            if res + k < r-l+1:
                m[nums[l]] -= 1
                l += 1
            
            if res + k >= r-l+1:
                ans = max(ans,res)

        return ans