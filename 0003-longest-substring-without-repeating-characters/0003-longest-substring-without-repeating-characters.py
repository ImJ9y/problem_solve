class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        L = 0
        charSet = set()
        sub_len = 0

        for R in range(len(s)):
            cur_c = s[R]
            while cur_c in charSet:
                charSet.remove(s[L])
                L += 1
            
            charSet.add(cur_c)
            sub_len = max(sub_len, R - L + 1)
    
        return sub_len
        

