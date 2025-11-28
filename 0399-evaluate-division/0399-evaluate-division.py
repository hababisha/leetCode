class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        
        def solve(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0

            stack = [(src, 1.0)]
            visited = set()

            while stack:
                node, cur_val = stack.pop()

                if node == dst:
                    return cur_val

                visited.add(node)

                for nei, weight in graph[node]:
                    if nei not in visited:
                        stack.append((nei, cur_val * weight))

            return -1.0
        
        ans = []
        for num, den in queries:
            ans.append(solve(num, den))

        return ans
