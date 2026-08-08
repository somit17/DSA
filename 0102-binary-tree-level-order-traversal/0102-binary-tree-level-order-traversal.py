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
        levels = []
        queue = deque([(root,0)])
        while queue:
            node,level_num = queue.popleft()
            if len(levels) == level_num:
                levels.append([node.val])
            else:
                levels[level_num].append(node.val)
            if node.left:
                queue.append((node.left,level_num+1))
            if node.right:
                queue.append((node.right,level_num+1))

        return levels