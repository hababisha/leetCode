# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = -1
        l = 1
        r = n
        while l <= r:
            mid = l + (r-l) // 2
            if isBadVersion(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans