# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        current = head
        total = 0
        while current:
            total+=1
            current = current.next
        
        del_node_count = total - n 
        prev = None
        current = head
        if del_node_count == 0:
            return head.next
        while del_node_count > 0:
            print(current.val)
            prev = current
            current = current.next
            del_node_count-=1
        prev.next = current.next
        return head