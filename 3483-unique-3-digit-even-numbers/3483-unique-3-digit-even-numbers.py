class Solution:
    def totalNumbers(self, digits):
        digits.sort()
        seen = set()
        n = len(digits)

        def backtrack(path, used):
            if len(path) == 3:
                if path[0] != 0 and path[-1] % 2 == 0:
                    num = path[0] * 100 + path[1] * 10 + path[2]
                    seen.add(num)
                return

            for i in range(n):
                if used[i]:
                    continue
               
                used[i] = True
                path.append(digits[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False]*n)
        return len(seen)
