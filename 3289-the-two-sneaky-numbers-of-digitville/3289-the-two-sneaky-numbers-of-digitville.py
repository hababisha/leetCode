class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        ans = set()
        for num in nums:
            if m[num] > 1:
                ans.add(num)
        return ist(ans)