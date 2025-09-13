class Solution:
    def maxFreqSum(self, s: str) -> int:
        vc = defaultdict(int)
        cc = defaultdict(int)

        for c in s:
            if c in "aeiou":
                vc[c] += 1
            else:
                cc[c] += 1
        
        mv = mc = 0

        for v in vc.values():
            mv = max(mv,v)
        
        for x in cc.values():
            mc = max(x, mc)
        
        return mv + mc
