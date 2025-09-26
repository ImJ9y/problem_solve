class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #Djikstra - shortest path (BFS) - min heap

        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))
        
        min_heap = [(0,k)]
        visit = set()
        result = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            result = max(result, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        
        return result if len(visit) == n else -1






