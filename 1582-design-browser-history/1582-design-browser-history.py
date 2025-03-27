class ListNode(object):
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur = ListNode(homepage)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.cur.next = ListNode(url, prev = self.cur)
        self.cur = self.cur.next
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        while self.cur.prev and steps > 0:
            steps -= 1
            self.cur = self.cur.prev
        
        return self.cur.val
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.next and steps > 0:
            steps -= 1
            self.cur = self.cur.next
        
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)