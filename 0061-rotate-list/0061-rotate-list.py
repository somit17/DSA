# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        length = 0
        current = head
        while current:
            current = current.next
            length+=1
        k = k % length
        if k == 0:
            return head
        upto = length - k - 1 
        current = head
        while upto > 0:
            current = current.next
            upto-=1
        new_head,next_ptr = current.next,current.next
        current.next = None 
        while next_ptr and next_ptr.next:
            next_ptr = next_ptr.next
        if next_ptr:
            next_ptr.next = head
        return new_head

        