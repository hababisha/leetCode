class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        incoming = defaultdict(int)

        for u,v in prerequisites:
            g[v].append(u)
            incoming[u] += 1
        q = deque()
        courses = []
        for i in range(numCourses):
            if incoming[i] == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            courses.append(c)
            for nei in g[c]:
                incoming[nei] -= 1

                if incoming[nei] == 0:
                    q.append(nei)
        if len(courses) == numCourses:
            return True
        else:
            return False
