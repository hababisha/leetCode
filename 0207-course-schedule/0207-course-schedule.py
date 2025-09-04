class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for u,v in prerequisites:
            graph[v].append(u)
            incoming[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                q.append(i)
        order = []
        while q:
            node = q.popleft()
            order.append(node)

            for nei in graph[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)
        return len(order) == numCourses
