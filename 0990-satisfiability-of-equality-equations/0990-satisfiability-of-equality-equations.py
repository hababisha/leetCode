class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]
        
        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            parent[p2] = p1
        

        for eq in equations:
            if eq[1] == "!":
                continue
            
            a = ord(eq[0]) - ord('a')
            b = ord(eq[3]) - ord('a')
            union(a, b)

        for eq in equations:
            if eq[1] != "!":
                continue
            a = ord(eq[0]) - ord('a')
            b = ord(eq[3]) - ord('a')
            if find(a) == find(b):
                return False
        return True