# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def recursive_approach(root):
            if not root:
                return
            recursive_approach(root.left)
            recursive_approach(root.right)
            values.append(root.val)
        recursive_approach(root)
        def iterative_approach(root):
            stack1,stack2 = [root],[]
            while stack1:
                node = stack1.pop()
                stack2.append(node)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)

            while stack2:
                values.append(stack2.pop().val)
            return 
        return values