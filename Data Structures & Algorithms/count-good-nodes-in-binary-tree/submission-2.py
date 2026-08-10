# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node,currMax):
            nonlocal res
            if not node:
                return 
            if (node.val >= currMax):
                res += 1
            currMax = max(node.val,currMax)
            dfs(node.left, currMax)
            dfs(node.right,currMax)

        dfs(root,root.val)
        return res
