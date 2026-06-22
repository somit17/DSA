# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse_recursive(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and traverse_recursive(p.left,q.right) and traverse_recursive(p.right,q.left)
        #return traverse_recursive(root.left,root.right)
        def traverse_iteratively(root):
            stack = [(root.left,root.right)]
            while(stack):
                l , r = stack.pop()
                if not l and not r:
                    continue
                if not l or not r or (l.val != r.val):
                    return False
                stack.append((l.left,r.right))
                stack.append((l.right,r.left))
            return True
        return traverse_iteratively(root)


