class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length = m + n - 1

        while m > 0 and n > 0 and length > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[length] = nums2[n-1]
                n -= 1
            else:
                nums1[length] = nums1[m-1]
                m -= 1
            length -= 1
        
        while m > 0:
            nums1[length] = nums1[m-1]
            m -= 1
            length -= 1
        
        while n > 0:
            nums1[length] = nums2[n-1]
            n -= 1
            length -= 1
        
        
