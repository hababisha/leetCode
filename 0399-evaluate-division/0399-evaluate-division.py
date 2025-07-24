class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        def bfs(i,j):
            if i not in graph or j not in graph:
                return -1
            q, visit= deque(), set()
            q.append([i, 1])
            visit.add(i)
            while q:
                node, product = q.popleft()
                if node == j:
                    return product
                for nei,weight in graph[node]:
                    if nei not in visit:
                        q.append([nei, product*weight])
                        visit.add(nei)
            return -1
        return [bfs(q[0], q[1]) for q in queries]            