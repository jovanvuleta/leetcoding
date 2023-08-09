from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        """
            Intuition: Memoization/bottom up approach
            Time complexity: O(N^2 * M)
            Space complexity: O(len(s) + 1)
        """

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


if __name__ == "__main__":
    print(Solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
