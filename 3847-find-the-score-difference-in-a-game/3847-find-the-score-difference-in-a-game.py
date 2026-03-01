class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        isFirst = True
        firstScore = secondScore = 0

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                isFirst = False if isFirst else True
            if i % 6 == 5:
                isFirst = False if isFirst else True

            if isFirst: firstScore += nums[i]
            else: secondScore += nums[i]
        return firstScore - secondScore