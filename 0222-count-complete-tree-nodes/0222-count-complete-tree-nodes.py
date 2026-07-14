# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs_approach(root):
            if not root:
                return 0
            stack = [root]
            count = 0
            while stack:
                node = stack.pop()
                count+=1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return count
        def bfs_approach(root):
            if not root:
                return 0
            queue = deque([root])
            count = 0
            while queue:
                node = queue.popleft()
                count+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return count
        return bfs_approach(root)

        