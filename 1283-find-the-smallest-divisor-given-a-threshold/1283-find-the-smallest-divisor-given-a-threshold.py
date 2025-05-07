class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        while l < r:
            mid = (l + r) // 2
            if sum((num + mid - 1) // mid for num in nums) <= threshold:
                r = mid
            else:
                l = mid + 1
        return l