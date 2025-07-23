class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hashMap = defaultdict(int)
        curS = 0
        l = 0
        for r in range(len(nums)):
            curS += nums[r]
            hashMap[nums[r]] += 1

            if r-l+1 > k:
                hashMap[nums[l]] -= 1
                if hashMap[nums[l]] == 0:
                    hashMap.pop(nums[l])
                curS -= nums[l]
                l += 1
            if len(hashMap) == (r-l+1) == k:
                res = max(res, curS)
        return res