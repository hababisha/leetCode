class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0] * 3
        for c in nums:
            bucket[c] += 1
        
        r, w, b = bucket
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b
                
