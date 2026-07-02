# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorderset = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        def recurse(l,r):
            if l > r:
                return None
            rootval = preorder[self.pre_idx]
            root = TreeNode(rootval)
            mid = inorderset[rootval]
            self.pre_idx += 1
            # root.left = TreeNode(inorder[idx - 1]) if inorder[idx -1] and inorder[idx-1] < root.val else None
            # root.right = TreeNode(inorder[idx + 1]) if inorder[idx + 1] and inorder[idx + 1] > root.val else None
            root.left = recurse(l, mid - 1)
            root.right = recurse(mid + 1, r)
            return root
        return recurse(0, len(preorder) -1)
        
                
