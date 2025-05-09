class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        ans = -1
        while l <= r:
            mid = l + (r - l ) // 2
            coinsNeeded = (mid/2) * (mid + 1)
            if coinsNeeded > n:
                r = mid - 1
            else:
                ans = l
                l = mid + 1
        return ans