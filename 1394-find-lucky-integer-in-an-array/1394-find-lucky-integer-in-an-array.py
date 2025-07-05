class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = Counter(arr)
        ans = -1
        for key,val in m.items():
            if key == val:
                ans = max(ans, key)
        return ans