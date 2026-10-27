"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node in self.map:
            return self.map[node]

        copy = Node(node.val)
        self.map[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.cloneGraph(neighbor))
        return copy