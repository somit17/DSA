# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_head = head
        total = 0
        while temp_head:
            temp_head = temp_head.next
            total+=1
        print(f'Total {total}')
        steps = total - k 
        current = head
        tail = head
        while k > 1:
            k-=1
            current = current.next
        while steps > 0:
            tail = tail.next
            steps-=1
        current.val,tail.val = tail.val,current.val
        print(f'Current_val - {current.val}')
        print(f'Tail_val - {tail.val}')
        return head