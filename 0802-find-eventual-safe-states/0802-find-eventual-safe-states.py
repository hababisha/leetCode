class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        UNVISITED, VISITING, VISITED =  0, 1, 2
        state = [UNVISITED]*n  
        def dfs(node):
            if state[node]:
                return state[node] == VISITED
            state[node] = VISITING  
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = VISITED  
            return True
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans