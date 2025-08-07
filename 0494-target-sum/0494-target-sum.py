class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)

        dp = [[0] * (2 *total +1) for _ in range(n + 1)]
        dp[0][total] = 1 

        for i in range(1, n + 1):
            for s in range(2 * total + 1):
                if dp[i - 1][s] > 0:
                    if s + nums[i-1] < 2 * total + 1:
                        dp[i][s + nums[i-1]] += dp[i -1][s]
                    if s - nums[i-1] >= 0:
                        dp[i][s - nums[i-1]] += dp[i - 1][s]

        return dp[n][target + total] if 0 <= target + total < 2 * total + 1 else 0
