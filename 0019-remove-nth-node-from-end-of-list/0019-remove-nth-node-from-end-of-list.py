# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        steps = 0
        length = 0
        temp_head = head
        while temp_head:
            length+=1
            temp_head = temp_head.next
        steps = length - n
        prev = None
        curr = head
        while steps > 0:
            prev = curr
            curr = curr.next
            steps-=1
        if prev is None:
            head=curr.next
        else:
            prev.next=curr.next
        return head

