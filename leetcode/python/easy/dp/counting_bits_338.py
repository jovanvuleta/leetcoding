from typing import List


class Solution:
    @staticmethod
    def countBits(n: int) -> List[int]:
        """
            Time complexity: O(log(2^N))
            Space complexity: O(N * log(N))
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp


if __name__ == "__main__":
    print(Solution.countBits(n=4))
