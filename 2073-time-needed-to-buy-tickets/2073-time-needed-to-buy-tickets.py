class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(0,k+1):
            if tickets[i] <= tickets[k]:
                res += tickets[i]
            else:
                res += tickets[k]
        for i in range(k+1, len(tickets)):
            if tickets[i] < tickets[k]:
                res += tickets[i]
            else:
                res += tickets[k] - 1
        return res