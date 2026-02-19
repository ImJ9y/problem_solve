class RecentCounter:

    def __init__(self):
        self.cache = collections.deque()

    def ping(self, t: int) -> int:

        self.cache.append(t)

        while self.cache[0] < t-3000:
            self.cache.popleft()
        
        return len(self.cache)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)