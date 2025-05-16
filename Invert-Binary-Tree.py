# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. base case: if root is None, we return None
# 2. we swap the values of the children
# 3. call recursion on the children if they exist 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root

        root.left, root.right = root.right, root.left
        if root.left: self.invertTree(root.left)
        if root.right: self.invertTree(root.right)

        return root