# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(root):
            if not root:
                return 0
            # if root:
            #     return root.val
            left = dfs(root.left)
            print(f'Left - > {left}')
            right = dfs(root.right)
            print(f'Right - > {right}')
            print(f'Current_root-val - > {root.val}')
            self.result += abs(left - right)
            return root.val + left + right

        dfs(root)
        return self.result