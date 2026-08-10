# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        n = 0
        cur = root
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            
            cur = st.pop()
            n += 1
            if (n == k):
                return cur.val
            cur = cur.right

        