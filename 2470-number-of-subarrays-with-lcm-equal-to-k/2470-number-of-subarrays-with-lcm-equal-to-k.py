class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            cur = 1
            for j in range(i, len(nums)):
                cur = lcm(cur, nums[j])
                if cur > k:
                    break
                if cur == k:
                    ans += 1

        return ans