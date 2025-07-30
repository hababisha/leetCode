class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:0, 1:0}

        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i-2]+dp(i-2), cost[i-1]+dp(i-1))
            return memo[i]
        return dp(len(cost))