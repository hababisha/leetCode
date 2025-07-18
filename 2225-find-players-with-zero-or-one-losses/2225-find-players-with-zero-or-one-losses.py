class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        sett = set()
        for w, l in matches:
            sett.add(w)
            sett.add(l)
        
        losers = {}
        winners = {}

        for w, l in matches:
            if w in winners:
                winners[w] += 1
            if w not in winners:
                winners[w] = 1
            if l in losers:
                losers[l] += 1
            if l not in losers:
                losers[l] = 1
        ans = [] 
        wlist = []
        llist = []
        for k in winners:
            if k not in losers:
                wlist.append(k)
        for j in losers:
            if losers[j] == 1:
                llist.append(j)
        wlist.sort()
        llist.sort()
        ans.append(wlist)
        ans.append(llist)

        return ans