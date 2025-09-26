class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cur = 0
        for i in range(31, -1, -1):
            cur <<= 1
            c = cur | 1
            pref = {num >> i for num in nums}
            found = False
            for p in pref:
                if (c ^ p) in pref:
                    found = True
                    break
            cur |= found
        
        return cur
