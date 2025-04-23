class RecentCounter:
    TIME_WINDOW = 3_000

    def __init__(self):
        self.data = deque()

    def ping(self, t: int) -> int:
        self.data.append(t)

        while self.data[0] < t - self.TIME_WINDOW:
            self.data.popleft()
        
        return len(self.data)