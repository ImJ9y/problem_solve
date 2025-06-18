class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        most_num = {0:0}

        for num in nums:
            if num in most_num:
                most_num[num] += 1
            else:
                most_num[num] = 1
        
        max_key = max(most_num, key=most_num.get)
    
        return max_key
            
        
