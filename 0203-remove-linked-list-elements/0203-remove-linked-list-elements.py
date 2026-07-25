# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummyNode = ListNode(0)
        current = dummyNode
        while head:
            if head.val != val:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return dummyNode.next
        