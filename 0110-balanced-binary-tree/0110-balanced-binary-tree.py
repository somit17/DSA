# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            height = 0
            queue = deque([root])
            while queue:
                current_level = len(queue)
                for i in range(current_level):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                height+=1
            return height
        def helper(root):
            if not root:
                return True
            left_subtree = height(root.left)
            right_subtree = height(root.right)
            if abs(left_subtree - right_subtree) > 1:
                return False
            return helper(root.left) and helper(root.right)
        return helper(root)
        