class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        pages = [0] * (len(citations)+1)

        for citation in citations:
            if citation >= len(citations):
                pages[-1] += 1
            else:
                pages[citation] += 1
        

        paper = pages[-1]
        h = len(citations)-1

        while h > paper:
            h -= 1
            paper += pages[h]
        
        return h