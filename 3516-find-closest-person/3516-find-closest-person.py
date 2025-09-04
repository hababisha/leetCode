class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) - abs(y-z) > 0:
            return 2
        elif abs(x-z) - abs(y-z) < 0:
            return 1
        
        return 0