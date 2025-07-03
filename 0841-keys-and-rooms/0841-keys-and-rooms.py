class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stk = [0]
        while stk:
            room = stk.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stk.append(key)

        return len(visited) == len(rooms)