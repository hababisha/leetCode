class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        l = 0
        r = len(letters) - 1

        while l <= r:
            mid = l + (r-l) // 2
            if letters[mid] > target:
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans
