class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = ''.join(map(str, digits))
        num = int(new) + 1
        neww = [int(digit) for digit in str(num)]
        return neww

        
    

        