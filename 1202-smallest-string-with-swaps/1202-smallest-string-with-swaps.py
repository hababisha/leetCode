class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(x, y):
            parent[find(x)] = find(y)

        for u, v in pairs:
            union(u, v)

        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)

        res = list(s)
        for indices in groups.values():
            chars = sorted([s[i] for i in indices])
            for idx, ch in zip(sorted(indices), chars):
                res[idx] = ch

        return "".join(res)
