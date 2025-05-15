# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#edge case if either of the tree is empty
#iterate through tree p
#pop the tuple contaning nodes of p and q
# compare them, return false early if any node isn't the same
# in the end, return true
from collections import deque
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False

        queue = deque([(p, q)])

        while queue:
            print(queue)
            cur_p, cur_q = queue.popleft()
            if  cur_p.val != cur_q.val: return False

            if cur_p.left and cur_q.left: queue.append((cur_p.left, cur_q.left)) 
            #if either has no left child
            elif cur_p.left or cur_q.left: return False
            if cur_p.right and cur_q.right: queue.append((cur_p.right, cur_q.right)) 
            #if either has no right child
            elif cur_p.right or cur_q.right: return False



        return True