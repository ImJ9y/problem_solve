# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res



        # stack = [(root, 0)]
        # res = []

        # while stack:
        #     node, depth = stack.pop()

        #     if depth == len(res):
        #         res.append([])
            
        #     res[depth].append(node.val)


        #     if node.right:
        #         stack.append((node.right, depth+1))
        #     if node.left:
        #         stack.append((node.left, depth+1))
        
        # return res
