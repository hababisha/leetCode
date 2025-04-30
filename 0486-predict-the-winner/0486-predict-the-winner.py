class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def ashu(left, right, a, b, turn):
            if left > right:
                return a >= b
        
            if turn:
                return (ashu(left+1, right, a+nums[left], b, 1 - turn) or
                        ashu(left, right-1, a+nums[right], b, 1 - turn))
            else:
                return (ashu(left+1, right, a, b+nums[left], 1 - turn) and          
                        ashu(left, right-1, a, b+nums[right], 1 - turn))
            
        
        return ashu(0, len(nums)-1, 0, 0, 1)