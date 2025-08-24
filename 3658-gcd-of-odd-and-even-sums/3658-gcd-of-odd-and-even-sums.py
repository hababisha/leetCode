class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        for i in range(1, 2*n,2):
            sumOdd += i
        for i in range(0, 2*n, 2):
            sumEven += i
        
        return math.gcd(sumOdd,sumEven)