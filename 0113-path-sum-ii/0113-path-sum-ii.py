# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node,rem_sum,path):
            if not node:
                return 
            path.append(node.val)
            rem_sum-=node.val
            if rem_sum==0 and node.left is None and node.right is None:
                result.append(path[:])
            dfs(node.left,rem_sum,path)
            dfs(node.right,rem_sum,path)
            path.pop()
        dfs(root,targetSum,[])
        return result