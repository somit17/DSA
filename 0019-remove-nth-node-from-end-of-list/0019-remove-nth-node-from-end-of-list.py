# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None:
            return head
        dummyNode = ListNode(0,head)
        slow,fast = dummyNode,head
        for _ in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        # print(f'S -> {slow}')
        # print(f'F -> {fast}')
        slow.next = slow.next.next
        return dummyNode.next
        