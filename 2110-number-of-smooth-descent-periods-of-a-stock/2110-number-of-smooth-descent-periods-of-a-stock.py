class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prices.append((10**5))
        ans = 0
        l,r = 0, 1
        while  r < len(prices):
            if prices[r] + 1 == prices[r-1]:
                r += 1
                continue
            n = r-l
            ans += (n * (n+1)) // 2
            l = r
            r += 1
        return ans


            