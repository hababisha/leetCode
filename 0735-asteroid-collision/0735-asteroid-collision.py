from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for n in asteroids:
            while stk and n < 0 < stk[-1]:
                if abs(n) > abs(stk[-1]):
                    stk.pop()
                    continue  
                elif abs(n) == abs(stk[-1]):
                    stk.pop()
                    break  
                else:
                    break
            else:
                stk.append(n)
        return stk
