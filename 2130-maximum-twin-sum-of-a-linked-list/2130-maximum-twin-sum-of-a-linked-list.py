# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # instead of reversing the second half reverse the first half
        # and move <--> in this direction while maximizing the sum
        slow,fast = head, head
        prev = None
        ans = 0
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while prev: # since n is even we could've used slow here
            ans = max(ans, prev.val + slow.val)
            slow = slow.next
            prev = prev.next
        return ans
