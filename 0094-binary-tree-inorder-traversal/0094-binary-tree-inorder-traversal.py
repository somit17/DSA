# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def recursive_approach(root):
            if not root:
                return
            recursive_approach(root.left)
            values.append(root.val)
            recursive_approach(root.right)
        #recursive_approach(root)

        def iterative_approach(root):
            stack=[]
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                values.append(root.val)
                root = root.right
        iterative_approach(root)
        return values