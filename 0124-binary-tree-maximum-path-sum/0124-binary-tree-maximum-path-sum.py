# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        max_sum = float('-inf')
        stack = [(root,False)]
        max_gain = {}
        while stack:
            node,visited = stack.pop()
            if not visited:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left,False))
                if node.right:
                    stack.append((node.right,False))
            else:
                left = max(0,max_gain.get(node.left,0))
                right = max(0,max_gain.get(node.right,0))
                max_gain[node] = node.val + max(left,right)
                max_sum = max(max_sum,node.val + left + right)

        return max_sum