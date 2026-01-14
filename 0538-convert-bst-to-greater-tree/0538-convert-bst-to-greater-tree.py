# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node: return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        suf = [0] * (len(arr)+1)
        for i in range(len(arr)-1, -1,-1):
            suf[i] = arr[i] + suf[i+1]

        m = {arr[i]: suf[i] for i in range(len(arr))}        
        def cons(node):
            if not node: return

            nt = TreeNode(m[node.val])
            nt.left = cons(node.left)
            nt.right = cons(node.right)
            return nt
        return cons(root)