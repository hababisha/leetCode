class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        tot = 0

        for arr,cook in customers:
            cur_time = max(cur_time, arr)
            cur_time += cook
            tot += cur_time - arr

        return tot/ len(customers)