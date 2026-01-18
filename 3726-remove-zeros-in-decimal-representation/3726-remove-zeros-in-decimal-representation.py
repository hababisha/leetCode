class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        k = 1

        while n > 0:
            ld = n % 10
            if ld != 0:
                ans +=  k * ld
                k *= 10
            n //= 10
        return ans