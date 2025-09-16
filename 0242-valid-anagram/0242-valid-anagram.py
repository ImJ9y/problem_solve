class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash_map = {}
        t_hash_map = {}

        for i in range(len(s)):
            if s[i] not in s_hash_map:
                s_hash_map[s[i]] = 1
            else:
                s_hash_map[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in t_hash_map:
                t_hash_map[t[j]] = 1
            else:
                t_hash_map[t[j]] += 1
        
        return s_hash_map == t_hash_map

