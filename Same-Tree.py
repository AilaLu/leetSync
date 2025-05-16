# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# intuition is to recursively call the tree, compare the two node throught the recursion, if not equal return false.
# if iterate through the entire tree and all comparision return true, return true
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p and not q:
          return True 
        # if p is null or q is null or they are not the same value
        if not p or not q:
            return False
        if  p.val != q.val:
            return False
        # recursive call for the children
        return  (self.isSameTree(p.right, q.right)) and (self.isSameTree(p.left, q.left))