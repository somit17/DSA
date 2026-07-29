# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Approach 1
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        result[:] = sorted(result)
        print(f'S- > {result}')
        dummyNode = ListNode(0)
        current = dummyNode
        for i in range(len(result)):
            current.next = ListNode(result[i])
            current = current.next
        return dummyNode.next