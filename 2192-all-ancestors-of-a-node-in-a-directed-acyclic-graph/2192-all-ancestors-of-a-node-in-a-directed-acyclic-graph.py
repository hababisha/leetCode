class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = [0] * n
        q = deque()

        for u, v in edges:
            graph[u].append(v)
            incoming[v] += 1

        ans = [set() for _ in range(n)] 

        for node in range(n):
            if incoming[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()

            for nei in graph[node]:
                ans[nei].add(node)  
                ans[nei].update(ans[node]) 

                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)

        return [sorted(list(ancestors)) for ancestors in ans]
