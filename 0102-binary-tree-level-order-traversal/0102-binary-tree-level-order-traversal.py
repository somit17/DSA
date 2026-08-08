# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # levels = []
        # queue = deque([(root,0)])
        # while queue:
        #     node,level_num = queue.popleft()
        #     if len(levels) == level_num:
        #         levels.append([node.val])
        #     else:
        #         levels[level_num].append(node.val)
        #     if node.left:
        #         queue.append((node.left,level_num+1))
        #     if node.right:
        #         queue.append((node.right,level_num+1))
        levels = []
        self.fill_levels(root,levels,0)
        return levels

    def fill_levels(self,root,levels,level_num):
        if root is None:
            return
        if len(levels) == level_num:
            levels.append([root.val])
        else:
            levels[level_num].append(root.val)
        left_paths = self.fill_levels(root.left,levels,level_num+1)
        right_paths = self.fill_levels(root.right,levels,level_num+1)