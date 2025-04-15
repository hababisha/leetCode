class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        ind = 0
        
        while curr is not None and ind != index:
            curr = curr.next
            ind += 1
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        if not self.head:
            self.head = new
            return
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        ind = 0
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        new = ListNode(val)
        while curr is not None and ind != index-1:
            curr = curr.next
            ind += 1
        if curr is None:
            return
        new.next = curr.next
        curr.next = new

    def deleteAtIndex(self, index: int) -> None:
        ind = 0
        curr = self.head
        if self.head is None:
            return 
        if index == 0:
            self.head = self.head.next
            return
        pre = None
        while curr is not None and ind!=index:
            pre = curr
            curr = curr.next
            ind += 1
        if curr is None:
            return 
        pre.next = curr.next
        