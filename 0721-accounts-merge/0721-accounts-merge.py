class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts) + 1)]
        emailToacc = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            p1, p2 = find(x), find(y)
            parent[p1] = p2

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToacc:
                    union(i, emailToacc[email])
                emailToacc[email] = i
        
        merged = {}
        for email, account_idx in emailToacc.items():
            root = find(account_idx)
            if root not in merged:
                merged[root] = set()
            merged[root].add(email)
        
        result = []
        for root, emails in merged.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))
        
        return result
        

