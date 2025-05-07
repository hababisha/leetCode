class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_indexes = deque([ index for  index, value in enumerate(senate) if value == "R"])
        d_indexes = deque([ index for  index, value in enumerate(senate) if value == "D"])


        while r_indexes and d_indexes:
            r = r_indexes.popleft()
            d = d_indexes.popleft()

            if r < d:
                c_i_r = r + len(senate)
                r_indexes.append(c_i_r)
            else:
                c_i_r = d + len(senate)
                d_indexes.append(c_i_r)
        return "Radiant" if r_indexes else "Dire"

