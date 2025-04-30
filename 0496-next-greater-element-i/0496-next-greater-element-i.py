class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monoInc, monoDec = [], []

        nextMap = defaultdict(lambda: -1)
        for n in nums2:
            while monoDec and monoDec[-1] < n:
                nextMap[monoDec.pop()] = n
            
            if monoInc and monoInc[-1] < n:
                nextMap[monoInc.pop()] = n
            
            monoInc.append(n)
        
        res = []
        for n in nums1:
            res.append(nextMap[n])
        return res