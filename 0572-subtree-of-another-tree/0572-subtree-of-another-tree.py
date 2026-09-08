# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        def valid(p, q):
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val:
                return False
            
            return (valid(p.left, q.left) and valid(p.right, q.right))
        
        if valid(root, subRoot):
            return True

        return (valid(root.left, subRoot) or valid(root.right, subRoot))