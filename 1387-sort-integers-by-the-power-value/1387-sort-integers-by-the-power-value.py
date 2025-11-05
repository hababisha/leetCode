class Solution:
    def calc(self, x, memo):
        if x == 1:
            return 0
        if x in memo:
            return memo[x]
        
        val = 0
        if x & 1:
            val = 1+self.calc(x*3+1, memo)
        else:
            val = 1+self.calc(x//2, memo)
        memo[x] = val
        return memo[x]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        heap = []

        for n in range(lo, hi+1):
            heap.append((self.calc(n,memo), n))

        heapq.heapify(heap)
        for _ in range(k):
            order, num = heapq.heappop(heap)
        return num