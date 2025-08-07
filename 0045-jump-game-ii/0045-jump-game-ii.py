class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i >= n - 1:
                return 0
            if i in memo:
                return memo[i]

            minn = float('inf')
            for j in range(1, nums[i] + 1):
                minn = min(minn, 1 + dp(i + j))

            memo[i] = minn
            return minn

        return dp(0)
