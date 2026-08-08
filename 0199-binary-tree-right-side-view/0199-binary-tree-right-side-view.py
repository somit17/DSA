# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        self.fill_levels(root, levels, 0)
        result = []
        for each_level in levels:
            result.append(each_level[-1])
        return result

    def fill_levels(self,root, levels, level_num):
        if not root:
            return
        
        if len(levels) == level_num:
            levels.append([root.val])  # Fixed: use root.val, not current.val
        else:
            levels[level_num].append(root.val)  # Fixed: use root.val
        
        self.fill_levels(root.left, levels, level_num + 1)
        self.fill_levels(root.right, levels, level_num + 1)