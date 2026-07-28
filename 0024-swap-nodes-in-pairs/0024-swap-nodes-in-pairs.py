# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #We need to swap values only
        if not head:
            return 
        current = head
        while current and current.next:
            current.val,current.next.val = current.next.val,current.val
            current = current.next.next
        return head
        