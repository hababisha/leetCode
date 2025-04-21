"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
      
        current = head
        while current:
            cloned_node = Node(current.val, current.next)
            current.next = cloned_node 
            current = cloned_node.next   
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next   
      
        original_current = head
        cloned_head = head.next
        while original_current:
            cloned_current = original_current.next
            original_current.next = cloned_current.next 
            if cloned_current.next:
                cloned_current.next = cloned_current.next.next
            original_current = original_current.next
      
        return cloned_head