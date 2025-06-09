class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        for n in nums1:
            nums.append(n)
        for m in nums2:
            nums.append(m)
        
        nums = sorted(nums)

        if len(nums) % 2 ==  0:
            m1 = nums[len(nums) // 2]
            m2 = nums[(len(nums) // 2) - 1]
            m = (m1 + m2) / 2
        else:
            m = nums[(len(nums) // 2)]
        
        return round(float(m), 5)
