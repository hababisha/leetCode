class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r 
        def canShip(cap):
            ships = 1
            curCapacity = cap

            for w in weights:
                if curCapacity - w < 0:
                    ships += 1
                    curCapacity = cap
                curCapacity -= w
            return ships <= days
        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                ans = cap
                r = cap - 1
            
            else:
                l = cap + 1
        return ans