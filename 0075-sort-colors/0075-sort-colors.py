class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minIdx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIdx]:
                    minIdx = j

            nums[i], nums[minIdx] = nums[minIdx], nums[i]          