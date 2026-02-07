class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n+2) for _ in range(n+2)]
        
        def lis(i, prev):
            if i == n:
                return 0

            if memo[i][prev] == -1:

                include = 0
                if prev == n+1 or nums[i] > nums[prev]:
                    include = 1 + lis(i + 1, i)

                exclude = lis(i + 1, prev)

                memo[i][prev] = max(include, exclude)
            
            return memo[i][prev]

        return lis(0, n+1)