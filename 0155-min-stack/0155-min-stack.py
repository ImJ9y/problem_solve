class MinStack(object):

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stk.append(val)
        val = min(val, self.min_stk[-1] if self.min_stk else val)
        self.min_stk.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        self.stk.pop()
        self.min_stk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()