class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dp(i, amount):
            if amount == 0:
                return 1
            if i < 0 or amount < 0:
                return 0
            if (i, amount) not in memo:
                include = dp(i, amount - coins[i])  
                exclude = dp(i - 1, amount)
                memo[(i, amount)] = include + exclude         
            return memo[(i,amount)]

        res = dp(n - 1, amount)
        return res 