
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        q = deque([root])

        while q:
            node = q.popleft()
            if node.val != val:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True
