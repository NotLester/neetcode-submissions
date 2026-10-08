class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        ahead = self.left.next
        self.left.next = node
        node.next = ahead

    def addAtTail(self, val: int) -> None:
        curr = self.left
        while curr.next and curr.next != self.right:
            curr = curr.next
        node = Node(val)
        ahead = self.right
        curr.next = node
        node.next = ahead

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left
        while curr.next and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr != self.right:
            node = Node(val)
            ahead = curr.next
            node.next = ahead
            curr.next = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left
        while curr.next and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr.next != self.right:
            ahead = curr.next.next
            curr.next = ahead


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)