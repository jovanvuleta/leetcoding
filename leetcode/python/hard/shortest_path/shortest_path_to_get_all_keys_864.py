import collections
from typing import List


class Solution:
    @staticmethod
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
            Desc: Bit mask is used here to keep track of the collected keys for relevant letter.
            Initially it will be 000.
            For collected key 'a', it would look like 001.
            For collected 'a' and 'b', it will be like 011.
            'a', 'b', 'c' -> 0111
            Time complexity: O(N * M)
            Space complexity: O(N * M)
        """
        visited = set()

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        q = collections.deque()

        rLen = len(grid)
        cLen = len(grid[0])

        cnt = 0
        start = None
        for row in range(rLen):
            for col in range(cLen):
                if grid[row][col].isalpha() and grid[row][col].islower():
                    cnt += 1
                if grid[row][col] == "@":
                    start = (row, col)

        q.append((start[0], start[1], 0, 0, 0))
        visited.add((start[0], start[1], 0))

        while q:
            row, col, steps, bitmask, keys = q.popleft()
            char = grid[row][col]
            if char.islower():
                pos = ord(char) - ord('a')
                # If a key hasn't been collected, take it(before 'a' -> 000, after collection 'a' -> 001)
                if bitmask & (1 << pos) == 0:
                    keys += 1
                    bitmask = bitmask | (1 << pos)

            if keys == cnt:
                return steps
            for dr, dc in directions:
                NR = row + dr
                NC = col + dc

                # 1. Checks if the next position is within the grid range
                # 2. Checks if the next position contains the same bitmask(state of the keys).
                #    If we have the same number of keys like before, we don't want to revisit this same position.
                if 0 <= NR < rLen and 0 <= NC < cLen and grid[NR][NC] != "#" and (NR, NC, bitmask) not in visited:

                    if char.isupper():
                        pos = ord(char) - ord('A')
                        # Checking if we have the key for the current char lock, if we do, we can add that
                        # (row, col) position in the queue
                        if bitmask & (1 << pos) != 0:
                            q.append((NR, NC, steps + 1, bitmask, keys))
                            visited.add((NR, NC, bitmask))
                    else:
                        q.append((NR, NC, steps + 1, bitmask, keys))
                        visited.add((NR, NC, bitmask))

        return -1


if __name__ == "__main__":
    print(Solution.shortestPathAllKeys(self=Solution, grid=["@..aA", "..B#.", "....b"]))
