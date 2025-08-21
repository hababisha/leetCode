class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for bit in range(32):
            cnt = 0
            for i in range(len(nums)):
                if nums[i] & (1 << bit):
                    cnt += 1
            
            if cnt%3:
                ans |= 1 << bit
        return ans