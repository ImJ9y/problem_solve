class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []

        line = []
        for num in nums1:
            if num not in nums2 and num not in line:
                line.append(num)
        
        res.append(line)
        line = []

        for num in nums2:
            if num not in nums1 and num not in line:
                line.append(num)
        res.append(line)

        return res