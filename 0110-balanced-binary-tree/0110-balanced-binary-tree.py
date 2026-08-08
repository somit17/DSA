# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            left_balanced = dfs(root.left)
            if left_balanced == -1:
                return -1
            right_balanced = dfs(root.right)
            if right_balanced == -1:
                return -1
            if abs(right_balanced - left_balanced) > 1:
                return -1
            return max(left_balanced,right_balanced) + 1
        return dfs(root)!=-1