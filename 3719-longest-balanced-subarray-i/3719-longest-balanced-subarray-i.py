class Solution:
    def longestBalanced(self, nums):
        ans = 0
        n = len(nums)

        for i in range(n):
            even = set()
            odd = set()
            for j in range(i,n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                
                if len(even) == len(odd):
                    ans = max(ans, j-i+1)
        return ans