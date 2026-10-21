# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def fill_levels(self,root,levels,level_num):
        if root is None:
            return 0
        if len(levels) == level_num:
            levels.append([root.val])
        else:
            levels[level_num].append(root.val)
        self.fill_levels(root.left,levels,level_num + 1)
        self.fill_levels(root.right,levels,level_num + 1)
        return len(levels)

         
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.fill_levels(root,[],0)
        # result = []
        # if not root:
        #     return 0
        # stack = [(root,0)]
        # while stack:
        #     current_node,lvl = stack.pop()
        #     if len(result) == lvl:
        #         result.append([current_node.val])
        #     else:
        #         result[lvl].append(current_node.val)
        #     if current_node.left:
        #         stack.append([current_node.left,lvl+1])
        #     if current_node.right:
        #         stack.append([current_node.right,lvl+1])
        # return len(result)

        


    def bfs(self,root):
        if root is None:
            return 0

        depth = 0
        queue = deque([root])
        
        while queue : 
            level_count = len(queue)
            for i in range(level_count):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return depth