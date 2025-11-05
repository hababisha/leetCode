# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(val = 1, next = head)
        if not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            value = math.gcd(prev.val, cur.val)
            node = ListNode(val=value)
            node.next = cur
            prev.next = node
            #update the pointers
            prev = cur
            cur = cur.next
        return head