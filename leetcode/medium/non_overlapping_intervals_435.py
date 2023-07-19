from typing import List


class Solution:
    @staticmethod
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            Intuition:
            Time complexity: O(N * log(N))
            Space complexity: O(1)
        """

        intervals.sort()

        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)
        return res


if __name__ == "__main__":
    print(Solution.eraseOverlapIntervals(self=Solution, intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
