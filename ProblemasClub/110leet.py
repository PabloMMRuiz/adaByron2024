# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.solve(root) is not None

    def solve(self, root: Optional[TreeNode]) -> int | None:
        if root.left is not None:
            l = self.solve(root.left)
        else:
            l = 0
        if root.right is not None:
            r = self.solve(root.right)
        else:
            r = 0

        if l is None or r is None or abs(r - l)>1:
            return None
        else:
            return max(r, l) + 1
        