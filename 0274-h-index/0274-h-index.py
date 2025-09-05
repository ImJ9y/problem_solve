class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        if len(citations)==1:
            return 1

        pages = [0] * (len(citations)+1)

        for citation in citations:
            if citation >= len(citations):
                pages[-1] += 1
            else:
                pages[citation] += 1
        
        print(pages)

        page = pages[-1]
        h = len(citations)-1

        print(page)
        print(h)

        while h > page:
            h -= 1
            page += pages[h]
        
        return h