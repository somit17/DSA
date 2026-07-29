"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        hash_map = {}
        current = head
        while current :
            hash_map[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            hash_map[current].next = hash_map.get(current.next)
            hash_map[current].random = hash_map.get(current.random)
            current = current.next
        return hash_map[head]
        