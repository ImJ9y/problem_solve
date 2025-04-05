# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def gcd(self, a, b):
            while b:
                a, b = b, a%b
            
            return a
    
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        cur = head

        while cur and cur.next:
            greatcommon = self.gcd(cur.val, cur.next.val)

            new_head = ListNode(greatcommon)
            new_head.next = cur.next
            cur.next = new_head

            cur = new_head.next
        
        return head