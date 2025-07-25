class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for i in range(len(recipes)):
            for j in ingredients[i]:
                graph[j].append(recipes[i])
                incoming[recipes[i]] += 1
        q = deque()
        for s in supplies:
            if incoming[s] == 0:
                q.append(s)
        
        ans = []
        sett = set(recipes)
        while q:
            node = q.popleft()
            if node in sett:
                ans.append(node)
            
            for nei in graph[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)
        return ans