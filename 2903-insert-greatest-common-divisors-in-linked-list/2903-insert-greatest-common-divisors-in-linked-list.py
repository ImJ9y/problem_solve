# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def helper(self, a, b):
        while b:
            a,b = b,a%b
        
        return a
    
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head

        while cur and cur.next:
            greatestCommon = self.helper(cur.val, cur.next.val)

            temp = cur.next
            
            new_head = ListNode(greatestCommon)
            new_head.next = cur.next
            cur.next = new_head

            cur = temp
        
        return head
            