# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        dummy = ListNode(0)
        dummy.next = head

        curr = head
        l = 0

        while curr:

            l += 1
            curr = curr.next

        check = dummy
        l -= n

        while  l > 0:

            l -= 1
            check = check.next

        check.next = check.next.next

        return dummy.next

            




