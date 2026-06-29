# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        print(result)
        result[left-1:right] = result[left-1:right][::-1]
        # print(result)
        dummyNode = ListNode(0,head)
        curr = dummyNode
        #count = len(result)
        for i in range(len(result)):
            curr.next = ListNode(result[i])
            curr = curr.next
        return dummyNode.next
