class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(curr):
            if curr > n:
                return
            ans.append(curr)
            for next_digit in range(10):
                generated_num = curr * 10 + next_digit
                if generated_num > n:
                    return
                
                dfs(generated_num)

        ans = []
        for start in range(1,10):
            dfs(start)
        return ans
        
