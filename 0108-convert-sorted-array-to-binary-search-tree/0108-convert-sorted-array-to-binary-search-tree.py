# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(lower,upper):
            if lower==upper:
                return None
            mid = (lower + upper) // 2
            node = TreeNode(nums[mid])
            node.left = helper(lower,mid)
            node.right = helper(mid+1,upper)
            return node
        return helper(0,len(nums))


        