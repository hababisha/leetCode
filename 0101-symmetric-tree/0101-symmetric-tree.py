# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(None)

            l = 0
            r = len(level) - 1
            while l < r:
                if level[l] == level[r]:
                    l += 1
                    r -= 1
                else:
                    return False
        return True
            