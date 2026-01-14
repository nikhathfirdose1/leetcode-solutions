class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1

        node = self.hm[key]
        self.remove(node)
        self.add(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:

        if key in self.hm:
            old_node = self.hm[key]
            self.remove(old_node)

        node = Node(key, value)
        self.add(node)
        self.hm[key] = node

        if len(self.hm) > self.capacity:
            least = self.head.next
            self.remove(least)
            del self.hm[least.key]

    
    def add(self,node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node


    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)