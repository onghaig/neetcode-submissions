# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #  root -> left and right -> if right > q, then continue on left only, and vice versa
        lt = p if p.val < q.val else q
        gt = q if q.val > p.val else p
        return self.searchTree(root, lt, gt)
        

    def searchTree(self, root, lt, gt):
        # find where it splits, that is the lowestCommonAncestor
        if (root.val > lt.val and root.val > gt.val):
            return self.searchTree(root.left, lt, gt)
        elif (root.val < lt.val and root.val < gt.val):
            return self.searchTree(root.right, lt, gt)
        else:
            return root