# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invertTree(root):
            if not root:
                return 
            root.left,root.right = root.right,root.left
            _invertTree(root.left)
            _invertTree(root.right)
        # _invertTree(root)
        # return root

        def dfs(root):
            if not root:
                return root
            stack = [root]
            while stack:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                left = node.left
                node.left = node.right
                node.right = left
            return root
        dfs(root)
        return root
        