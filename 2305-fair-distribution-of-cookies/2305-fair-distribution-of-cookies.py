class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(index):
            if index >= len(cookies):
                self.best_distribution = min(self.best_distribution, max(children_cookies))
                return
          
            for j in range(k):
                if children_cookies[j] + cookies[index] >= self.best_distribution or (j > 0 and children_cookies[j] == children_cookies[j - 1]):
                    continue
              
                children_cookies[j] += cookies[index]
                dfs(index + 1)
                children_cookies[j] -= cookies[index]
      
        self.best_distribution = float('inf')
        children_cookies = [0] * k
        cookies.sort(reverse=True)
        dfs(0)
        return self.best_distribution