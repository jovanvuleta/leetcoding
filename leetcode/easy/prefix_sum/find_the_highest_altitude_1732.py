from typing import List


class Solution:
    @staticmethod
    def largestAltitude(gain: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        max_alt = 0
        curr_alt = 0

        for i in range(0, len(gain)):
            curr_alt += gain[i]
            if curr_alt > max_alt:
                max_alt = curr_alt

        return max_alt


if __name__ == "__main__":
    print(Solution.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))
