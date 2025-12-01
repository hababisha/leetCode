class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)
        ans = [0,0]
        for i in range(len(nums1)):
            if nums1[i] in n2:
                ans[0] += 1
        
        for i in range(len(nums2)):
            if nums2[i] in n1:
                ans[1] += 1
        
        return ans