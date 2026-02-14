class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        self.line = []

        def check(num, num_list, line):
            if num not in num_list and num not in self.line:
                self.line.append(num)

        for num in nums1:
            check(num, nums2, [])
        
        res.append(self.line)

        self.line = []
        for num in nums2:
            check(num, nums1, [])
        
        res.append(self.line)

        return res