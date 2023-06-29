from collections import deque


class Solution:
    @staticmethod
    def predictPartyVictory(self, senate: str) -> str:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        senate = list(senate)
        r, d = deque(), deque()
        d = deque()

        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            r_top = r.popleft()
            d_top = d.popleft()

            if r_top < d_top:
                r.append(r_top + len(senate))
            else:
                d.append(d_top + len(senate))

        return "Radiant" if r else "Dire"


if __name__ == "__main__":
    print(Solution.predictPartyVictory(self=Solution, senate="RDD"))
