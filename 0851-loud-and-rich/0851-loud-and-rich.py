class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        incoming = defaultdict(int)

        for u,v in richer:
            graph[u].append(v)
            incoming[v] += 1
        
        q = deque()
        ans = [i for i in range(n)]
        for i in range(n):
            if incoming[i] == 0:
                q.append(i)
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for child in graph[node]:
                    incoming[child] -= 1

                    if incoming[child] == 0:
                        q.append(child)
                    
                    if quiet[ans[node]] <= quiet[ans[child]]:
                        ans[child] = ans[node]
        return ans