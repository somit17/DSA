# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Approach 1 traverse all
        # result  = []
        # while head:
        #     result.append(head.val)
        #     head = head.next
        # l,r = 0 , len(result) - 1
        # while l<=r:
        #     if result[l]!=result[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        #Approach 2
        slow,fast = ListNode(0,head),head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse(head):
            prev = None
            current = head
            while current:
                next_ptr = current.next
                current.next=prev
                prev = current
                current = next_ptr
            return prev
        first = head
        second = reverse(slow.next)
        while second:
            if first.val!=second.val:
                return False
            first = first.next
            second = second.next
        return True   