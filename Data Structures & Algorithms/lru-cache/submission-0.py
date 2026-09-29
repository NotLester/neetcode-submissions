class Node:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.size = capacity
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
            
        node = self.hashmap[key]
        self._remove(node)
        self._insert(node)
        
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        elif len(self.hashmap) == self.size:
            self._remove(self.head.next)
            
        new_node = Node(value, key)
        self._insert(new_node)

    def _remove(self, node) -> None:
        prev_n, next_n = node.prev, node.next
        prev_n.next, next_n.prev = next_n, prev_n
        del self.hashmap[node.key]
    
    def _insert(self, node) -> None:
        prev_n, next_n = self.tail.prev, self.tail
        prev_n.next = next_n.prev = node
        node.prev, node.next = prev_n, next_n
        self.hashmap[node.key] = node