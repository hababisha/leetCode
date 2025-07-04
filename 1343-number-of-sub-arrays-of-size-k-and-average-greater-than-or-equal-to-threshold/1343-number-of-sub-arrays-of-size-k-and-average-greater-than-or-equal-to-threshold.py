class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = sum(arr[:k])
        avg = summ // k
        l = 0
        c = 0
        if avg >= threshold:
            c += 1
        
        for r in range(k,len(arr)):
            summ = (summ + arr[r]) - arr[l]
            l += 1
            avg = summ//k
            if avg >= threshold:
                c += 1
        
        return c