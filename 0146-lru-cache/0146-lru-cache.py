class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.hm = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1 

        node = self.hm[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.hm:
            old_node = self.hm[key]
            self.remove(old_node)

        new_node = ListNode(key,value)
        self.hm[key] = new_node
        self.add(new_node)

        if len(self.hm)  > self.capacity:
            least = self.head.next
            self.remove(least)
            del self.hm[least.key]


    def add(self, node):
        last = self.tail.prev
        node.next = self.tail
        node.prev = last
        last.next = node
        self.tail.prev = node


    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)