class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        R = len(nums1)-1

        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[R] = nums2[n-1]
                n -= 1
            else:
                nums1[R] = nums1[m-1]
                m -= 1
            
            R -=1
        
        while m:
            nums1[R] = nums1[m-1]
            m -= 1
            R -= 1

        while n:
            nums1[R] = nums2[n-1]
            n -= 1
            R -= 1
     


