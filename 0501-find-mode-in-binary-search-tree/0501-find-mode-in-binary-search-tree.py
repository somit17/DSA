# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #approach 1 Using extra memory
        # result = []
        # def inorder(root):
        #     if not root:
        #         return 
        #     inorder(root.left)
        #     result.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # counter = Counter(result)
        # max_freq = max(counter.values())
        # result = []
        # for val, count in counter.items():
        #     if count == max_freq:
        #         result.append(val)
        # return result

        #approach 2
        self.curr_num = 0
        self.curr_freq = 0
        self.max_freq = 0
        self.result = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            
            if self.curr_num == root.val:
                self.curr_freq += 1
            else:
                self.curr_num = root.val
                self.curr_freq = 1
            
            if self.curr_freq > self.max_freq:
                self.max_freq = self.curr_freq
                self.result = [self.curr_num]
            elif self.curr_freq == self.max_freq:
                self.result.append(self.curr_num)
            
            dfs(root.right)
        
        dfs(root)
        return self.result