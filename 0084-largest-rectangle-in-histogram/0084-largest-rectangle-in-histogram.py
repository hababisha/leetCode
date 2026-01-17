class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk =[]

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                index, heigh = stk.pop()
                ans = max(ans,heigh * (i - index))
                start = index
            stk.append((start, h))
        
        for i, h in stk:
            ans = max(ans, h * (len(heights) - i))
        return ans