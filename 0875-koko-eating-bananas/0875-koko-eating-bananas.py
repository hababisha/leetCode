class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #  [3,6,7,11], h = 8
        # 1 
        # 11 max(piles) 
        def sheCanEat(m):
            c=0
            for p in piles:
                c  += math.ceil(p / m)
            return c <= h
        l, r= 1, max(piles)

        ans = -1
        while l <= r:
            m = (l + r) // 2
            if sheCanEat(m):
                ans  = m
                r = m - 1
            else:
                l  = m + 1
            
        return ans
