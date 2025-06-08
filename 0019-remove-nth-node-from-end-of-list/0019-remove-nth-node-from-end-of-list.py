# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1
        
        if length - n == 0:
            return head.next
        
        cur = head
        for i in range(length-n-1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head