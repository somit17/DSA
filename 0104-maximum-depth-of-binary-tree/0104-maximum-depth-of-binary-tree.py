# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Using BFS Approach
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            depth+=1
        return depth

        