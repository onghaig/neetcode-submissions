# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we will have to use dfs of some kind
        res = []
        nth = k
        def dfs(root,res):
            if not root:
                return 
            dfs(root.left,res)
            res.append(root.val)
            # if (nth == 0):
            #     return root.val
            # nth -= 1
            dfs(root.right,res)
        dfs(root,res)
        return res[k-1]
