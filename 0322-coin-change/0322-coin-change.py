class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins.sort(reverse=True)
        ans = 0
        for c in coins:
            while amount >= c:
                amount -= c
                ans += 1
        return ans if amount == 0 else -1

        greedy can solve this but it doesn't guarantee the optimal answer
        it fails because the denominations are arbitrary here
        eg. {1, 3, 4} and a target amount of 6.
            -> greedy approach would be sorting in descending order and then taking 4 and 2 1's, total amount of coins used here will be 3
            -> but we can use 2 3's and it's the answer so greedy fails
        """
        n = len(coins)
        memo = {}
        def dp(i, amount):
            if amount == 0:
                return 0
            if i < 0 or amount < 0:
                return float('inf')
            if (i, amount) not in memo:
                include = 1 + dp(i, amount - coins[i])  
                exclude = dp(i - 1, amount)
                memo[(i, amount)] = min(include, exclude)            
            return memo[(i,amount)]

        res = dp(n - 1, amount)
        return res if res != float('inf') else -1