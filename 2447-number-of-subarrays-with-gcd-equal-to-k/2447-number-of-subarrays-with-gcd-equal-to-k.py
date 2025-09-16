class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur = gcd(cur, nums[j])
                if cur < k:
                    break
                if cur == k:
                    ans += 1

        return ans