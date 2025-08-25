class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        while b != 0:
            summ = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = summ, carry

        return a if a <= MAX else ~(a ^ mask)
