# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        current = head
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #print(f'SLOW - {slow}')
        #print(f'HEAD  - {head}')
        second = self.reverseLinkedList(slow)
        slow.next = None
        #return head == second
        p1 = head
        p2 = second
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
    def reverseLinkedList(self,head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
        