class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r 
        def canShip(cap):
            days_used = 1
            curW = 0
            for w in weights:
                if curW + w > cap:
                    days_used += 1
                    curW = 0
                curW += w
            return days_used <= days

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                ans = cap
                r = cap - 1
            
            else:
                l = cap + 1
        return ans