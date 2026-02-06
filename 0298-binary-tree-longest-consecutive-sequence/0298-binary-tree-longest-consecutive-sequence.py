# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longestpath = 0

        def dfs(root, prev, length):
            if not root:
                return
            
            if root.val-1 == prev:
                length += 1
                self.longestpath = max(self.longestpath, length)

                dfs(root.left, root.val, length)
                dfs(root.right, root.val, length)
            else:
                dfs(root.left, root.val, 1)
                dfs(root.right, root.val, 1)
            
        dfs(root, root.val-1, 0)
        return self.longestpath