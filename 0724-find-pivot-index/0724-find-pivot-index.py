class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0] * len(nums)
        pref[0] = nums[0]

        suff = [0] * len(nums)
        suff[-1] = nums[-1]
        for i in range(1,len(nums)):
            pref[i] = nums[i] + pref[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suff[i] = nums[i] + suff[i+1]
        

        for i in range(len(nums)):
            if pref[i] == suff[i]:
                return i
        return -1