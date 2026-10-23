# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root,False)]
        height = {}
        diameter = 0
        while stack:
            node,visited = stack.pop()
            if not visited:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left,False))
                if node.right:
                    stack.append((node.right,False))
            else:
                l_tree = height.get(node.left,0)
                r_tree = height.get(node.right,0)
                height[node] = 1 + max(l_tree,r_tree)
                diameter = max(diameter,l_tree + r_tree)
        return diameter
                
        