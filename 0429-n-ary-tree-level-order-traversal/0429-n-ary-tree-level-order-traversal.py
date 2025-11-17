"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()
                level.append(curNode.val)
                for child in curNode.children:
                    q.append(child)
            ans.append(level)
        return ans
