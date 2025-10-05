class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            u,v = edges[i]
            weight = succProb[i]
            graph[u].append((v,weight))
            graph[v].append((u, weight))
        
        heap = [(-1, start_node)]
        visit = set()
        while heap:
            prob, cur = heapq.heappop(heap)
            visit.add(cur)

            if cur == end_node:
                return -prob
            
            for nei, edgeProb in graph[cur]:
                if nei not in visit:
                    heapq.heappush(heap, (prob*edgeProb, nei))
            
        return 0
            
