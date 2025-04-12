class MyStack(object):

    def __init__(self):
        self.stack = collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.appendleft(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.stack else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()