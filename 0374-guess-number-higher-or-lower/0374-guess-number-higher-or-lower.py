# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= n:
            mid = l + (r-l) // 2
            resp = guess(mid)
            if resp == 0:
                return mid
            elif resp == -1:
                r = mid -1
            else:
                l = mid + 1
