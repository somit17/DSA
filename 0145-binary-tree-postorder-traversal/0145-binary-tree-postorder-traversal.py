# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse_recursive(root):
            if not root:
                return 
            traverse_recursive(root.left)
            traverse_recursive(root.right)
            result.append(root.val)

        traverse_recursive(root)
        return result
        