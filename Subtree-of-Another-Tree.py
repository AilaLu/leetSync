# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#edge case:
# return true if subRoot is None
# return false if root is None
# create a helper function sameTree to check if two trees are the same
#for the helper function:
#base case: return true if both trees are None 
#if tree one and tree two vals are not the same, return false
#return sameTree(root.left) and samtree(root.right)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #null is always the subtree of any tree
        if not subRoot: return True
        #if root is null, subtree can never be found
        if not root: 
            return False
        #check if root node is already the same with subRoot
        if self.sameTree(root, subRoot): return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
         
    def sameTree(self, t_1, t_2):
        #both node are None
        if not t_1 and not t_2: return True
        #either one is None
        if not t_1 or not t_2: 
            return False
        if t_1.val != t_2.val: return False

        return self.sameTree(t_1.left, t_2.left) and self.sameTree(t_1.right, t_2.right)
