# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        num1,num2 = 0,0
        for n in reversed(s1):
            num1 = num1 * 10 + n
        for n in reversed(s2):
            num2 = num2 * 10 + n
        
        total  = num1 + num2
        if total == 0:
            return ListNode(0)
        dummy = ListNode(0)
        current = dummy
        for digit in reversed(str(total)):
            current.next = ListNode(int(digit))
            current = current.next
        return dummy.next
