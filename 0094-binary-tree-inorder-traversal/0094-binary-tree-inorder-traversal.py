# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(root:Optional[TreeNode]): #Recursive approach
            if not root:
                return 
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        #helper(root)
        #Using stack
        def stackhelper(root:Optional[TreeNode]):
            stack = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                result.append(root.val)
                root = root.right
        stackhelper(root)
        return result
        