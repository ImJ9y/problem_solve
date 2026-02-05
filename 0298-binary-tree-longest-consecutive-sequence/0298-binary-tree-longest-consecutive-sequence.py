# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longestpath = 0
        def dfs(cur, prev, length):
            if cur:
                if cur.val -1 == prev:
                    length += 1
                    self.longestpath = max(self.longestpath, length)

                    dfs(cur.left, cur.val, length)
                    dfs(cur.right, cur.val, length)
                else:
                    dfs(cur.left, cur.val, 1)
                    dfs(cur.right, cur.val, 1)
        
        dfs(root, root.val-1, 0)
        return self.longestpath
