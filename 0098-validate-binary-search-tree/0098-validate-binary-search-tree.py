# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_check(root,min_val,max_val):
            if not root:
                return True

            if root.val >= max_val or root.val <= min_val:
                return False
            
            left = dfs_check(root.left,min_val,root.val)
            right = dfs_check(root.right,root.val,max_val)
            return left and right
        return dfs_check(root,float('-inf'),float('inf'))
