class ListNode():

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def add(self, node):
        val = self.tail.prev
        val.next = node
        node.prev = val
        node.next = self.tail
        self.tail.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:

        if key not in self.dic:
            return -1 

        node = self.dic[key]
        self.remove(node)
        self.add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.dic:
            old = self.dic[key]
            self.remove(old)

        node = ListNode(key, value)

        self.dic[key] = node

        self.add(node)


        if len(self.dic) > self.capacity:

            to_del = self.head.next
            self.remove(to_del)
            del self.dic[to_del.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)