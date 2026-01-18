# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        ans = 0
        max_depth = 0

        while q:
            cand, depth = q.popleft()
            if depth > max_depth:
                ans = 0
                max_depth= depth
            if depth == max_depth:
                ans += cand.val
            
            if cand.left: q.append((cand.left, depth+1))
            if cand.right: q.append((cand.right, depth+1))
        return ans