# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lst = []
        def traverse(node):
            if not node: return

            traverse(node.left)
            lst.append(node.val)
            traverse(node.right)

        traverse(root)

        def construct(lst):
            if not lst: return None
            mid = len(lst) // 2
            ntree = TreeNode(lst[mid])
            ntree.left = construct(lst[:mid])
            ntree.right = construct(lst[mid+1:])
            return ntree
        return construct(lst)
