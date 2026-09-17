# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root: return []

        stack = [(root, 0)]
        res = []

        while stack:
            node, depth = stack.pop()

            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)

            if node.right:
                stack.append((node.right, depth+1))
            
            if node.left:
                stack.append((node.left, depth+1))
        
        return res