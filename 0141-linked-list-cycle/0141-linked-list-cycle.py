# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        met = False
        while fast and fast.next and fast.next.next and fast.next.next.next:
            fast = fast.next.next.next.next
            slow = slow.next

            if slow and fast and slow.val == fast.val:
                met = True
                break
        return met 

        