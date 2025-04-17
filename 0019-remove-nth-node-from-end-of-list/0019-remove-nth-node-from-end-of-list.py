# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        target = length - n
        i = 0

        dummy = ListNode()
        dummy.next = head
        prev, current = dummy, head
        i = 0 
        while current.next and i < target:
            prev = current
            current = current.next
            i += 1
        prev.next = current.next
        return dummy.next
        
