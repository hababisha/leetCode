class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        a = head
        b = a.next
        def swap(a,b):
            c = b.next
            b.next = a
            
            if c and c.next:
                a.next = swap(c, c.next)
            else:
                a.next = c
            return b
        head = swap(a,b)
        return head