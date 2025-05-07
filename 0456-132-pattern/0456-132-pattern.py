class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        thirdVal = float('-inf')
        stack = []
        for number in reversed(nums):
            if number < thirdVal:
                return True
            while stack and stack[-1] < number:
                thirdVal = stack.pop()
            stack.append(number)
        return False