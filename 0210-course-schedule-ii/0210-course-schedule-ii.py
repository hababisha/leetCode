class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        q = deque()
        
        for u,v in prerequisites:
            graph[v].append(u)
            incoming[u] += 1
        
        for crs in range(numCourses):
            if incoming[crs] == 0:
                q.append(crs)
 
        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in graph[node]:
                incoming[nei] -= 1
                
                if incoming[nei] == 0:
                    q.append(nei)
                
        return ans if len(ans) == numCourses else []

