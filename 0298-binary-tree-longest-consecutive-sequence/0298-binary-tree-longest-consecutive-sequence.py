# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 1

        def dfs(cur, pre_val, length):
            if cur:
                if cur.val-1 == pre_val:
                    length += 1
                    self.longest_path = max(self.longest_path, length)
                    dfs(cur.left, cur.val, length)
                    dfs(cur.right, cur.val, length)
                else:
                    dfs(cur.left, cur.val, 1)
                    dfs(cur.right, cur.val, 1)

        dfs(root, root.val, 0)

        return self.longest_path
