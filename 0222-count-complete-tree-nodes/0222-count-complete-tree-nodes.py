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
            return dfs_approach(root.left)+dfs_approach(root.right)+1
        #return dfs_approach(root)  

        def bfs_approach(root):
            if not root:
                return 0
            queue = deque([root])
            count = 0
            while queue : 
                level_size = len(queue)
                for i in range(level_size):
                    node = queue.popleft()
                    count+=1
                    if node and node.left:
                        queue.append(node.left)
                    if node and node.right:
                        queue.append(node.right)
            return count
        return bfs_approach(root)
