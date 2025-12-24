class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def bt(i, curT):
            if curT == target:
                res.append(sol[:])
                return
            if i >= len(candidates) or curT > target:
                return

            sol.append(candidates[i])
            bt(i, curT + candidates[i])  
            sol.pop()

            bt(i + 1, curT)

        bt(0, 0)
        return res
       