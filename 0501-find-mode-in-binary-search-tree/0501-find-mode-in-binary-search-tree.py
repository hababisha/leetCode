# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        m = Counter(ans)
        mode = max(m.values())
        res = []
        for k,v in m.items():
            if v == mode:
                res.append(k)
        return res