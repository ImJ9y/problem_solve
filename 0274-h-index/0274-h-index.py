class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        paper_count = [0] * (len(citations)+1)

        for citation in citations:
            if citation >= len(citations):
                paper_count[-1] += 1
            else:
                paper_count[citation] += 1

        h = len(citations)
        paper = paper_count[h]

        while paper < h:
            h -= 1
            paper += paper_count[h]
        
        return h