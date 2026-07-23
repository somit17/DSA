# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        def bfs(root):
            queue = deque([root])
            while queue:
                level_size = len(queue)
                temp = []
                for i in range(level_size):
                    current_node = queue.popleft()
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                    temp.append(current_node.val)
                result.append(temp)
                    
        bfs(root)
        return result 
        