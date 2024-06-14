# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Mismo código que problema 100 pero espejo
    def isSameTreeMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val != q.val:
            return False
        if p.val == q.val:
            return True and self.isSameTreeMirror(p.left,q.right) and self.isSameTreeMirror(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSameTreeMirror(root.left, root.right)
