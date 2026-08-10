# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we will have to use dfs of some kind
        # res = []
        res = root.val
        nth = k
        def dfs(root):
            nonlocal nth, res
            if not root:
                return
            dfs(root.left)
            if (nth == 0):
                return
            nth -= 1
            if (nth == 0):
                res = root.val
                return
            # if (nth == 0):
            #     return root.val
            # nth -= 1
            dfs(root.right)
        dfs(root)
        return res        
