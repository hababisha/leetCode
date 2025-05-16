class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def sumEvens(arr):
            s = 0
            for n in nums:
                if n%2 == 0:
                    s += n
            return s
        ans = [0] * len(nums)
        for i in range(len(queries)):
            idx = queries[i][1]
            val = queries[i][0]
            nums[idx] += val
            ans[i] = sumEvens(nums)
        return ans

