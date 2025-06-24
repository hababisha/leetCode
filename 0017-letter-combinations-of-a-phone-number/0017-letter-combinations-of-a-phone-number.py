class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
      
        digit_to_chars = {  "2":'abc',
                            "3": 'def',
                            "4":'ghi',
                            "5":'jkl',
                            "6": 'mno', 
                            "7":'pqrs', 
                            "8":'tuv', 
                            "9":'wxyz'}
        res = []
        

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digit_to_chars[digits[i]]:
                backtrack(i+1, curStr +c)

        backtrack(0, "")
        return res