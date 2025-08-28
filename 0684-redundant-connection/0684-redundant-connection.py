class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]
        
        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            parent[p2] = p1
        
        for u,v in edges:
            if find(u) == find(v):
                return [u,v]
            union(u,v)
