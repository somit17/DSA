# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(head,prev = None):
            if head is None:
                return prev
            next_ptr = head.next
            head.next = prev
            return recursive(next_ptr,head)
        # if not head:
        #     return 
        # current = head
        # prev = None
        # while current:
        #     next_ptr = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_ptr
        return recursive(head)
        #return prev
        