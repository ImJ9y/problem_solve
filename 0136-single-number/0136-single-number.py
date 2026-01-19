class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Because every number except one appears exactly twice, the duplicate numbers will eventually pair up and "cancel" each other out to become 0.Example walkthrough with nums = [2, 2, 1]:Start: res = 0First 2: 0 ^ 2 = 2Second 2: 2 ^ 2 = 0 (The pair cancels out)The 1: 0 ^ 1 = 1Result: 1 (The single number remains)This approach is ideal for your goal of becoming a software engineer because it meets the strict interview constraints: it runs in linear time ($O(n)$) and uses constant extra space ($O(1)$).

        ans = 0
        for num in nums:
            ans ^= num
        
        return ans

        # seen = []

        # for num in nums:
        #     if num in seen:
        #         seen.remove(num)
        #     else:
        #         seen.append(num)
        
        # return seen[0]