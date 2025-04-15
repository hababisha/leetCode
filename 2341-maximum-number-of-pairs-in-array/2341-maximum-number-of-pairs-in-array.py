class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        pair,left = 0, 0
        ans = []
        for k in m:
            pair += m[k] // 2
            if m[k] % 2 == 1:
                left += 1 
        return [pair, left]

        
        