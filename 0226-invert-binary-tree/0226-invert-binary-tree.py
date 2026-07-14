# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return
        # left_subtree = self.invertTree(root.left)
        # right_subtree = self.invertTree(root.right)
        # root.left = right_subtree
        # root.right = left_subtree
        # return root
        def dfs(root):
            if not root:
                return 
            stack = [root]
            while stack:
                node = stack.pop()#4
                if node.left:
                    stack.append(node.left) #7
                if node.right:
                    stack.append(node.right) #2
                left_node = node.left
                node.left = node.right
                node.right = left_node
            return root
        return dfs(root)
