# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse_recursive(root):
            if not root:
                return 
            result.append(root.val)
            traverse_recursive(root.left)
            traverse_recursive(root.right)
        #traverse_recursive(root)

        def traverse_iterative(root):
            if not root:
                return
            stack = [root]
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)        
        traverse_iterative(root)
        return result