# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recSum(root, path, nums:list):

    if not root.left and not root.right:
        nums.append(int(path+str(root.val),2))
    else:
        if root.left:
            recSum(root.left, path+str(root.val), nums)
        if root.right:
            recSum(root.right, path+str(root.val), nums)

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums = []
        recSum(root, "", nums)
        return sum(nums)