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
        queue = deque([root])
        result = []
        while queue:
            level_size=len(queue)
            temp = []
            for i in range(level_size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                temp.append(current.val)
            result.append(temp)
        return result    
            