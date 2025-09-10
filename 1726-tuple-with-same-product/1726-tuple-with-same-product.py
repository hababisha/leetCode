class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                ans += 8 * m[prod]
                m[prod] += 1
        return ans
                
        