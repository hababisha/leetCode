class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent =  [i for i in range(len(points))]
        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]
        def union(x,y):
            p1, p2 = find(x), find(y)
            parent[p1] = p2



        temp = []
        for i in range(len(points) - 1):
            for j in range(len(points)):
                Xi, Yi = points[i]
                Xj, Yj = points[j]
                t = abs(Xi - Xj) + abs(Yi - Yj)
                temp.append((t, i, j))
        temp.sort()
        res = 0
        for t in temp:
            val, i, j = t
            t1 = find(i)
            t2 = find(j)
            if t1 != t2:
                union(i, j)
                res += val

        return res
