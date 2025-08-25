class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0] * (len(arr)+1)
        for i in range(len(arr)):
            pref[i+1] = pref[i] ^ arr[i]
        # print(pref)
        ans = []
        for q1, q2 in queries:
            ans.append(pref[q2+1]^pref[q1])
        return ans
