# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True

        def valid(p, q):
            if not p and not q:
                return True
            
            if not(p and q and p.val == q.val):
                return False
            else:
                return valid(p.left, q.left) and valid(p.right, q.right)
        

        if valid(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))