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
        
        copy_old = {None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copy_old[cur] = copy

            cur = cur.next
        
        cur = head
        while cur:
            copy = copy_old[cur]
            copy.next = copy_old[cur.next]
            copy.random = copy_old[cur.random]

            cur = cur.next
        
        return copy_old[head]