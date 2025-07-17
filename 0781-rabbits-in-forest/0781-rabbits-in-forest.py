class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        r = 0
        for n in freq:
            if freq[n] < (n+1):
                r = r + n + 1
            else:
                r += math.ceil(freq[n]/(n+1)) * (n+1)


        return r
