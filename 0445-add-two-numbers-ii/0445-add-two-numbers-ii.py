# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def revLL(head):

            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        r1 = revLL(l1)
        r2 = revLL(l2)

        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while r1 != None or r2 != None or carry != 0:

            r1_val = r1.val if r1 else 0
            r2_val = r2.val if r2 else 0

            value = (r1_val + r2_val + carry) % 10
            carry = (r1_val + r2_val + carry) // 10

            new_node = ListNode(value)
            curr.next = new_node
            curr = curr.next

            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None


        return revLL(dummy.next)
