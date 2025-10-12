class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for n in nums:
            prod *= n
        
        ans = [0]*len(nums)
        for i in range(len(nums)):
            res = 1
            if nums[i] == 0:
                for j in range(len(nums)):
                    if i == j:
                        continue
                    res *= nums[j]
                ans[i] = res
            else:
                ans[i] = prod // nums[i] 
        return ans