import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # #BFS
        # queue = collections.deque([root])
        # num_depth = 0

        # while queue:
        #     num_depth += 1
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
    
        #DFS
        stack = [(root, 1)]
        num_depth = 0
        while stack:
            node, depth = stack.pop()
            num_depth = max(num_depth, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))

        return num_depth