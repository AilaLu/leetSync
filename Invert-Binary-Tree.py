# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
\\\
✅ Recursive Approach
Style: Simpler, more concise code.

Mechanism: Uses the call stack for tree traversal.

Downside: Risk of stack overflow for very deep trees (e.g., skewed trees).

✅ Iterative Approach
Style: Uses an explicit stack or queue (DFS or BFS).

Mechanism: Manages its own memory, avoiding call stack limits.

Advantage: Safer for deep trees or environments with recursion limits.
\\\

#recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #edge case:
        if not root: return None
        root.right, root.left = root.left, root.right
        #recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root