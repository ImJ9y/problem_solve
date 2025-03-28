class ListNode(object):
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        i = 0
        cur = self.left.next

        while cur:
            if i == index and cur.next:
                return cur.val
            i += 1
            cur = cur.next
        
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_head = ListNode(val)
        next = self.left.next
        prev = self.left

        next.prev = new_head
        prev.next = new_head

        new_head.next = next
        new_head.prev = prev



    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_head = ListNode(val)
        next = self.right
        prev = self.right.prev

        next.prev = new_head
        prev.next = new_head

        new_head.next = next
        new_head.prev = prev



    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.left.next

        while cur and index > 0:
            index -= 1
            cur = cur.next
        
        if index == 0 and cur:
            new_head = ListNode(val)
            next = cur
            prev = cur.prev

            next.prev = new_head
            prev.next = new_head

            new_head.next = next
            new_head.prev = prev



    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur = self.left.next

        while cur and index > 0:
            index -= 1
            cur = cur.next
        
        if index == 0 and cur and cur.next:
            next = cur.next
            prev = cur.prev

            next.prev = prev
            prev.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)