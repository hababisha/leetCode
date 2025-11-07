class Solution:
    def frequencySort(self, s: str) -> str:
        m = Counter(s)
        sK = lambda x : (-m, x)
        return "".join(sorted(s, key=sK))