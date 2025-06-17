class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        close_sum = nums[0] + nums[1] + nums[2]
        close_distance = abs(target - close_sum)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums)-1

            while L < R:
                cur_sum = nums[i] + nums[L] + nums[R]
                cur_dis = abs(target - cur_sum)


                if cur_sum == target:
                    return target
                elif cur_dis < close_distance:
                    close_sum = cur_sum
                    close_distance = cur_dis
                

                if cur_sum < target:
                    L += 1
                else:
                    R -= 1
                
        return close_sum