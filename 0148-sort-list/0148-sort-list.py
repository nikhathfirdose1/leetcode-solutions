# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_sort(head):
            if not head or not head.next:
                return head

            mid = getMid(head)
            left = merge_sort(head)
            right = merge_sort(mid)


            return merge(left,right)

        
        def merge(head1, head2):
            dummy = ListNode(0)
            res = dummy

            while head1 and head2:
                if head1.val <= head2.val:
                    res.next = head1
                    head1 = head1.next
                else:
                    res.next = head2
                    head2 = head2.next

                res = res.next

            res.next = head1 if head1 else head2

            return dummy.next




        def getMid(head):

            fast = head
            slow = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None

            return slow 


        return merge_sort(head)
        







        

            


