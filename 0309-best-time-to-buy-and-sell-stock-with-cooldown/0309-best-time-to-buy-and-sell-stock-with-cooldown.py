class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}  

        def dp(i, bought, soldYesterday):
            if i == len(prices):
                return 0
            if (i, bought, soldYesterday) in memo:
                return memo[(i, bought, soldYesterday)]

            if bought:
                sell = prices[i] + dp(i+1, False, True)
                skip = dp(i+1, True, False)
                ans = max(sell, skip)
            else:
                buy = 0
                if not soldYesterday:
                    buy = -prices[i] + dp(i+1, True, False)
                not_buy = dp(i+1, False, False)
                ans = max(buy, not_buy)

            memo[(i, bought, soldYesterday)] = ans
            return ans

        return dp(0, False, False)

