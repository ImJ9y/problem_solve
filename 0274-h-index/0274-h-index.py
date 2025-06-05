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
        
        

        h = len(citations)
        paper = papers[h]

        print(papers)
        print(h)
        print(paper)

        while paper < h:
            h -= 1
            paper += papers[h]
        
        return h