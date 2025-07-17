class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        b = 0

        for char in s:
            if char == "R":
                b += 1
            if char == "L":
                b -= 1
            if b == 0:
                c += 1
        return c