
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        stk = []
        stk.append(root)
        while stk:
            node = stk.pop()
            if node.val != val:
                return False
            if node.left: stk.append(node.left)
            if node.right: stk.append(node.right)
        return True