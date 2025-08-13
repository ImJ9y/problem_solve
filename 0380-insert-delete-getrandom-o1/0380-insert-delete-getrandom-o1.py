class RandomizedSet(object):

    def __init__(self):
        self.array = []
        self.valuesIndex = {} #value : index -> we need O(1) solution

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.valuesIndex:
            return False
        
        self.valuesIndex[val] = len(self.array)
        self.array.append(val)

        return True

    
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.valuesIndex:
            return False
        
        index = self.valuesIndex[val]

        self.valuesIndex[self.array[-1]] = index
        del self.valuesIndex[val]
        self.array[index] = self.array[-1]
        self.array.pop()

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()