# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #We need to swap values only
        # if not head:
        #     return 
        # current = head
        # while current and current.next:
        #     current.val,current.next.val = current.next.val,current.val
        #     current = current.next.next
        # return head

        #Approach 2
        dummy = ListNode(0,head)
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next
        