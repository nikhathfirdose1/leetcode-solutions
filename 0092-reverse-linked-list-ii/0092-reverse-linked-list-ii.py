# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:


        if not head:
            return None

        
        dummy = ListNode(0)
        dummy.next = head
        before = dummy

        for i in range(left - 1):
            before = before.next


        prev = before
        curr = before.next

        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        before.next.next = curr
        before.next = prev


        return dummy.next