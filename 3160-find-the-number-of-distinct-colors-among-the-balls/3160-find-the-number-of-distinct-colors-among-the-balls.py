class Solution:
    def queryResults(self, limit, queries):
        '''
        btc -> {} maps ball to color
        colorFreq = {} maps color to freq
        ans = []
        loop through the queries
            if b in btc:
                colorFreq[btc[b]] -= 1
                if colorFreq[btc[b]] == 0:
                    pop the color from the colorFreq

            colorFreq[color] = 1 + colorFreq.get(color, 0)
            ans.append(len(colorFreq))
            btc[b] = c

        '''
        btc = {}
        colorFreq = {}
        ans = []
        for ball, color in queries:
            if ball in btc:
                colorFreq[btc[ball]] -= 1
                if colorFreq[btc[ball]] == 0:
                    colorFreq.pop(btc[ball])
            colorFreq[color] = 1 + colorFreq.get(color, 0)
            ans.append(len(colorFreq))
            btc[ball] = color
        return ans

