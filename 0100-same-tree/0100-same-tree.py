# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _isSameTree(p,q) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and (_isSameTree(p.left,q.left) and _isSameTree(p.right,q.right))
        #return _isSameTree(p,q)

        def dfs_iterative(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            stack = [(p,q)]
            while stack:
                node1,node2 = stack.pop()
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                stack.append((node1.left,node2.left))
                stack.append((node1.right,node2.right))
            return True

        def bfs_approach(p,q):
            queue = deque([(p, q)])
            while queue:
                node1, node2 = queue.popleft()
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False  
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            return True
        return bfs_approach(p,q)
