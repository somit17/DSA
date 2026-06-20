# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Approach 1
        #using extra space
        seen = set()
        result_values = [] 
        curr = head
        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                result_values.append(curr.val)
            curr = curr.next

        dummyNode = ListNode(0)
        current = dummyNode
        for value in result_values:
            current.next = ListNode(value)
            current = current.next
        return dummyNode.next
        