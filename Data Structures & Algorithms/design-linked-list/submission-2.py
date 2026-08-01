class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.d_head = ListNode()
        self.d_tail = ListNode()
        self.d_head.next = self.d_tail
        self.d_tail.prev = self.d_head
        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        if index < (self.size // 2):
            res = self.d_head
            for _ in range(index):
                res = res.next
            return res
        
        res = self.d_tail.prev
        for _ in range(self.size - index):
            res = res.prev
        return res

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        new_node = ListNode(val)
        prev = self.getPrev(index)
        next = prev.next

        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node

        self.size += 1

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