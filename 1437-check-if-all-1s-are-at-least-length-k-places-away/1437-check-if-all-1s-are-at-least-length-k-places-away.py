class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l = 0

        for r in range(1, len(nums)):
            if nums[r]:
                if nums[l] != 1:
                    continue
                if r - l - 1 < k:
                    return False
            
                
            l += 1
        return True