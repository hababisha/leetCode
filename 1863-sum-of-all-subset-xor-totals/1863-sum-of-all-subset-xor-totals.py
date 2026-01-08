class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res, subs = [], []

        def bt(i):
            if i >= len(nums):
                res.append(subs[:])
                return

            subs.append(nums[i])
            bt(i+1)
            subs.pop()

            bt(i+1)
        bt(0)
        print(res)
        ans = 0
        for sub in res:
            xor = 0
            for el in sub:
                xor ^= el
            ans += xor
        return ans