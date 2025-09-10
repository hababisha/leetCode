class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x, y = min(nums), max(nums)

        for i in range(x, -1, -1):
            if x % i==0 and y % i == 0:
                return i
