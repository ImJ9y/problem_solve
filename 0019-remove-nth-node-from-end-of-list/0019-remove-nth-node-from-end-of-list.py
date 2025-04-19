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
        count = 0

        while cur:
            count += 1
            cur = cur.next
        
        cur = head
        if count - n == 0:
            return head.next

        for i in range(count - n - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head