class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    
    def __init__(self):
        self.dummy_head = self.tail = ListNode(0)
    
    def get(self, index: int) -> int:
        curr = self.dummy_head
        
        while index >= 0 and curr:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.dummy_head:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        old_head = self.dummy_head.next
        new_node = ListNode(val, old_head)
        self.dummy_head.next = new_node
        if self.tail == self.dummy_head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        beforeTarget = self.dummy_head
        
        while index >= 1 and beforeTarget:
            beforeTarget = beforeTarget.next
            index -= 1
        
        if not beforeTarget or not beforeTarget.next:
            return False
        
        if self.tail == beforeTarget.next:
            self.tail = beforeTarget
            
        new_next = beforeTarget.next.next
        beforeTarget.next = new_next
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.dummy_head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
