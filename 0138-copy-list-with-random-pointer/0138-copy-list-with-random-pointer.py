"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old_copy = {None:None}
        cur = head

        while cur:
            copy = Node(cur.val)
            old_copy[cur] = copy

            cur = cur.next
        
        cur = head
        while cur:
            copy = old_copy[cur]
            copy.next = old_copy[cur.next]
            copy.random = old_copy[cur.random]

            cur = cur.next
        
        return old_copy[head]