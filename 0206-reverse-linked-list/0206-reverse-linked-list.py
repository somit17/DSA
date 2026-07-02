# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head
        # while curr:
        #     next_ptr = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_ptr
        # return prev
        
        #recursive
        if head is None or head.next is None:
            return head
        prev = None
        h2 = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return h2
        