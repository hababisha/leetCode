class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3  
        max_coins = 0
        for i in range(1, 2 * n, 2):  
            max_coins += piles[i]

        return max_coins

        