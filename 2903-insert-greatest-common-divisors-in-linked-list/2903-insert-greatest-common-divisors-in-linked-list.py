# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        cur = head

        while cur and cur.next:
            greatestCommon = 0
            divide = min(cur.val, cur.next.val)
            for i in range(1, divide+1):
                if cur.val%i == 0 and cur.next.val%i == 0:
                    greatestCommon = i

            new_head = ListNode(greatestCommon)

            new_head.next = cur.next
            cur.next = new_head

            cur = new_head.next
        
        return head
        