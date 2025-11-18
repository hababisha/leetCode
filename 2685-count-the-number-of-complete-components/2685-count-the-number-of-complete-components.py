class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def bfs(node):
            q = deque([node])
            visited.add(node)
            nodes,childCount = 0,0
            while q:
                node = q.popleft()
                nodes += 1

                for nei in graph[node]:
                    childCount += 1
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            print(nodes, childCount)
            return nodes * (nodes -1)== childCount
        c = 0
        for i in range(n):
            if i in visited: continue
            if bfs(i):
                c += 1
        return c