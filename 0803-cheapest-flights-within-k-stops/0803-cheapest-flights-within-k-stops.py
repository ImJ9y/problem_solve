class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman-ford
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s, d, p in flights: #s = sources, d = destination, p = price
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float('inf') else -1