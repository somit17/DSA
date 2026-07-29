# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseLinkedList(root):
            if not root:
                return 
            prev = None
            current = root
            while current:
                next_ptr = current.next
                current.next = prev
                prev = current
                current = next_ptr
            return prev
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = reverseLinkedList(slow.next)
        slow.next = None
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next 
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        