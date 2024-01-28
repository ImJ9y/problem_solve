# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
 
        # Use set to store unique values in linked list
        unique_vals = set()
        curr = head  # Pointer to traverse the linked list
        prev = None  # Pointer to keep track of the previous node
 
        # Iterate through the linked list
        while curr:
            # If the current value already exists in set, remove the node
            if curr.val in unique_vals:
                prev.next = curr.next
            else:
                # Otherwise, add the value to set and move on to the next node
                unique_vals.add(curr.val)
                prev = curr
            curr = curr.next
 
        # Return the head of the linked list
        return head