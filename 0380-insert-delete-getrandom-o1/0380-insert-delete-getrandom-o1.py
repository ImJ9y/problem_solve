class RandomizedSet(object):

    def __init__(self):
        self.stk = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.stk:
            return False
        else:
            self.stk.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.stk:
            self.stk.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.stk)  


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()