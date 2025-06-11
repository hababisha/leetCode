class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
      
        digit_to_chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
      
        combinations = ['']
      
        for digit in digits:
            letters = digit_to_chars[int(digit) - 2]
          
            combinations = [prefix + letter for prefix in combinations for letter in letters]
      
        return combinations