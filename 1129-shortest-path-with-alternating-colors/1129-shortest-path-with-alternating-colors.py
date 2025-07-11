class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        visited = set()
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)
        
        q = deque()
        q.extend([(0,1),(0,-1)])
        visited.add((0,1))
        visited.add((0,-1))
        for u, v in redEdges:
            redGraph[u].append(v)
        for u, v in blueEdges:
            blueGraph[u].append(v)
        
        length = 0
        while q:
            for _ in range(len(q)):
                node, color  = q.popleft()
                if ans[node] == -1:
                    ans[node] = length
                if color == 1:
                    for nei in redGraph[node]:
                        if (nei, -1) not in visited:
                            q.append((nei, -1))
                            visited.add((nei,-1))
                if color == -1:
                    for nei in blueGraph[node]:
                        if (nei, 1) not in visited:
                            q.append((nei, 1))
                            visited.add((nei,1))
            
            length += 1
        

        return ans
