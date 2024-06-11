class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if left == 0:
                return right+1
            if right == 0:
                return left+1
            return min(left, right)+1