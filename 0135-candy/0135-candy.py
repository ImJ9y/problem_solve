class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        candies = [1] * len(ratings)
        
        for i in range(1, length):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1
        
        for i in range(length-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)
