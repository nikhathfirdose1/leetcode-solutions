# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        heap = []
        dummy = ListNode(0)
        res = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))


        while heap:
            val, i, node = heapq.heappop(heap)

            res.next = node
            res = res.next
            

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

            


        