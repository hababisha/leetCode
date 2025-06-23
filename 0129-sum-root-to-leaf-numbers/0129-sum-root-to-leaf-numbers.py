# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        path=0
        def dfs(node,path):
            if not node:
                return 0
            path = path * 10 + node.val
            if not node.left and not node.right:
                return path
            return dfs(node.left,path)+dfs(node.right,path)
            

        return dfs(root,path)
        