class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        parent = [i for i in range(N)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            px, py = find(x), find(y)
            parent[px] = py
        xs = collections.defaultdict(list)
        ys =  collections.defaultdict(list)

        for i, (x, y) in enumerate(stones):
            xs[x].append(i)
            ys[y].append(i)
        

        for x in xs.keys():
            index = xs[x][0]
            for index2 in xs[x][1:]:
                union(index,index2)
        
        for y in ys.keys():
            index = ys[y][0]
            for index2 in ys[y][1:]:
                union(index, index2)
        
        seen= set()
        for index in range(N):
            seen.add(find(index))
        return N - len(seen)