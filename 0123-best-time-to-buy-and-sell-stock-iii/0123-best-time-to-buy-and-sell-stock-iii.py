class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        
        def dp(day, t, bought):
            if day >= n:
                return 0
            if t == 0:
                return 0
            if memo[day][t][bought] != -1:
                return memo[day][t][bought]
            
            if bought: 
                sell = prices[day] + dp(day+1, t-1, not bought)  
                not_sell = dp(day+1, t, bought)
                memo[day][t][bought] = max(sell, not_sell)
            else:  
                buy = -prices[day] + dp(day+1, t, not bought)  
                skip = dp(day+1, t, bought) 
                memo[day][t][bought] = max(buy, skip)
            
            return memo[day][t][bought]
        
        return dp(0, 2, False)
