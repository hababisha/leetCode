class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        ans = 0
        n = len(heights)

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                area = w*h
                ans = max(area, ans)
                start = j
            stk.append((height, start))
        
        while stk:
            h, j = stk.pop()
            w = n-j
            area = w * h
            ans = max(area, ans)
        return ans
