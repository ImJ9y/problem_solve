# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # cur, res = root, []

        # while cur or res:
        #     while cur:
        #         res.append(cur)
        #         cur = cur.left
            
        #     cur = res.pop()
        #     k -= 1
        #     if k == 0:
        #         return cur.val

        #     cur = cur.right

        queue = collections.deque([root])
        res = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        
        res.sort()
        return res[k-1]

        