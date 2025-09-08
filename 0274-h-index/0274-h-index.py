class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        papers = [0] * (len(citations)+1)

        for citation in citations:
            if citation >= len(citations):
                papers[-1] += 1
            else:
                papers[citation] += 1
        
        
        h = len(papers)-1
        paper = papers[-1]

        while h > paper:
            h -= 1
            paper += papers[h]
        
        return h
