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
        dummyNode = ListNode()
        dummyNode.next = head
        prev, cur = dummyNode, head
        i = 0
        while cur.next and i < target:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = cur.next
        return dummyNode.next