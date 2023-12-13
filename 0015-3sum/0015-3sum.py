class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #To arrange smallest to largest
        nums.sort()
        answer = []
        
		#Need to add Three values
        for i in range(len(nums)-2):
			#if index i and i-1 are duplicated, move to next
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total < 0:
                    #Because we sorted it earlier so Left side is smallest
                    #Need to make sum larger
                    L += 1
                elif total > 0:
                    #Need to make sum smaller
                    R -= 1
                else:
                    #when total == 0
                    triplet = [nums[i],nums[L],nums[R]]
                    answer.append(triplet)
                    #Check duplicate
                    while L < R and nums[L] == triplet[1]:
                        L += 1
                    while L < R and nums[R] == triplet[2]:
                        R -= 1
            
        return answer
    
                    
        