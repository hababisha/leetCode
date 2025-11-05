class Solution:
    def restoreArray(self, adj: List[List[int]]) -> List[int]:
        ans = []
        graph = defaultdict(list)

        for u,v in adj:
            graph[u].append(v)
            graph[v].append(u)
        
        st = adj[0][0]
        for k, v in graph.items():
            if len(v) == 1:
                st = k
                break
        
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei in graph[node]:
                if nei in seen:
                     continue
                dfs(nei)
            ans.append(node)
        dfs(st)
        return ans
