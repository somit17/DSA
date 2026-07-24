# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        dummyNode = ListNode(0)
        current = dummyNode
        while list1 and list2:
            if list1.val > list2.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            current = current.next
        if list1:
            current.next=list1
        if list2:
            current.next = list2
        print(dummyNode)
        return dummyNode.next
        