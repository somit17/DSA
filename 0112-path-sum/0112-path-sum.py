# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Iterative
        def dfs_iterative(root):
            if not root:
                return False
            stack = [(root,root.val)]
            while stack:
                node , currentSum = stack.pop()
                if node.left is None and node.right is None and currentSum == targetSum:
                    return True
                if node.left:
                    stack.append((node.left,node.left.val + currentSum))
                if node.right:
                    stack.append((node.right,node.right.val + currentSum))
            return False
        def dfs_recursive(root,targetSum):
            if not root:
                return False
            if root.left is None and root.right is None and root.val == targetSum:
                return True
            return dfs_recursive(root.left,targetSum - root.val) or dfs_recursive(root.right,targetSum - root.val)
        
        return dfs_recursive(root,targetSum)