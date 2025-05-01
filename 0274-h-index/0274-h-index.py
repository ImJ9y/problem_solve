class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        paper_pages = [0] * (len(citations)+1)

        for i in range(len(citations)):
            if citations[i] > len(citations):
                paper_pages[-1] += 1
            else:
                paper_pages[citations[i]] += 1
        
        
        h = len(citations)
        page = paper_pages[h]

        while h > page:
            h -= 1
            page += paper_pages[h]
        
        return h