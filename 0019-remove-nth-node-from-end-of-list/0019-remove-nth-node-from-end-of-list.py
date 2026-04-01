# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 step (on one pass get the length of the list)
        dummy = ListNode(0, head)
        k = 0
        cur = head
        while cur:
            k += 1
            cur = cur.next
        
        
        # 2 step is getting the k - n node
        cur = dummy
        for _ in range(k-n):
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next
        