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
        # dummy_list = ListNode(0, head)
        # left = dummy_list
        # right = head

        # while n > 0 and right:
        #     n -= 1
        #     right = right.next
        
        # while right:
        #     left = left.next
        #     right = right.next
        
        # left.next = left.next.next

        # return dummy_list.next

        cur = head
        count = 0

        while cur:
            count += 1
            cur = cur.next
        
        if count - n == 0:
            return head.next

        cur = head
        for i in range(count - n - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head