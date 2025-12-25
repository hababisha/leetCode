class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        happy,ans = 0,0
        for i in range(k):
            if happiness[i] - happy >= 0:
                ans += (happiness[i] - happy)
            happy += 1
        return ans