# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode()
        temp = merged
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
            
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return merged.next
        

#         # Initialize a dummy node for the merged list
#         merged = ListNode()
#         # Create a temporary pointer to traverse and build the merged list
#         temp = merged

#         # Continue merging while both list1 and list2 have nodes
#         while list1 and list2:
#             # Compare values of the current nodes in list1 and list2
#             if list1.val < list2.val:
#                 # If the value in list1 is smaller, add it to the merged list
#                 temp.next = list1
#                 # Move the pointer in list1 to the next node
#                 list1 = list1.next
#             else:
#                 # If the value in list2 is smaller or equal, add it to the merged list
#                 temp.next = list2
#                 # Move the pointer in list2 to the next node
#                 list2 = list2.next
            
#             # Move the temporary pointer in the merged list to the newly added node
#             temp = temp.next

#         # Check if there are remaining nodes in list1 or list2
#         if list1:
#             # If there are remaining nodes in list1, add them to the merged list
#             temp.next = list1
#         else:
#             # If there are remaining nodes in list2, add them to the merged list
#             temp.next = list2

#         # Return the merged list starting from the next of the dummy node
#         return merged.next