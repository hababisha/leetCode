class Solution:
    def superPow(self, base: int, exponent_digits: List[int]) -> int:
        mod = 1337
        res = 1

        for d in reversed(exponent_digits):
            res = (res * pow(base, d, mod)) % mod
            base = pow(base, 10, mod)
      
        return res
