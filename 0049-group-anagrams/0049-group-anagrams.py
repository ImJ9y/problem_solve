class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:
        answer = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 #a...z (26 characters)
            
            for c in s:
                #ord() - change to unicode character
                #a = 80
                #b = 81
                #c = 82
                count[ord(c)-ord('a')] += 1
            
            answer[tuple(count)].append(s)
#defaultdict(<type 'list'>, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): [u'eat']})
 
        return answer.values()
        
#         or

#         answer = defaultdict(list)

#         for s in strs:
#             answer["".join(sorted(s))].append(s)

#         return answer.values()