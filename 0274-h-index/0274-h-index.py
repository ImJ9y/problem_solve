class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        paper_count = [0] * (length+1)
        i = 0

        for i in range(length):
            if citations[i] >= length:
                paper_count[-1] += 1
            else:
                paper_count[citations[i]] += 1
        
        h = len(citations)
        paper = paper_count[h]

        while paper < h:
            h -= 1
            paper += paper_count[h]
        
        return h