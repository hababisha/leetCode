class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        sett = set(nums1)
        for n in nums2:
            if n in sett:
                ans.append(n)
        return list(set(ans))