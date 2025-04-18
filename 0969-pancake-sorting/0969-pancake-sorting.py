class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        x = len(arr)

        for i in range(x):
            max_ = max(arr[:x-i])
            maxInd = arr.index(max_) + 1
            arr[:maxInd] = reversed(arr[:maxInd])
            ans.append(maxInd)
            arr[:x-i] = reversed(arr[:x-i])
            ans.append(x-i)
        return ans