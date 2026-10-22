# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        result = self.helper(root,[],0)
        return result[::-1]
    
    def helper(self,root,levels,level_num):
        if not root:
            return []

        if len(levels) == level_num:
            levels.append([root.val])
        else:
            levels[level_num].append(root.val)
        
        self.helper(root.left,levels,level_num + 1)
        self.helper(root.right,levels,level_num + 1)
        return levels