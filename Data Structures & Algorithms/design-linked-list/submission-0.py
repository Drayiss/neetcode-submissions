class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_tail.prev = self.dummy_head
        self.dummy_head.next = self.dummy_tail
        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        if index <= (self.size // 2):
            prev = self.dummy_head
            for _ in range(index):
                prev = prev.next
            return prev
        
        prev = self.dummy_tail.prev
        for _ in range(self.size - index):
            prev = prev.prev
        return prev


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def insertNode(self, val: int, prev: ListNode, next: ListNode) -> None:
        new_node = ListNode(val)
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.size += 1

    def addAtHead(self, val: int) -> None:
        self.insertNode(val, self.dummy_head, self.dummy_head.next)

    def addAtTail(self, val: int) -> None:
        self.insertNode(val, self.dummy_tail.prev, self.dummy_tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        prev = self.getPrev(index)
        self.insertNode(val, prev, prev.next)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        prev = self.getPrev(index)
        next = prev.next.next
        prev.next = next
        next.prev = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)