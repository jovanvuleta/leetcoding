class Solution:
    @staticmethod
    def repeatedSubstringPattern(s: str) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        ds = (s + s)[1: -1]
        return s in ds

    @staticmethod
    def repeatedSubstringPatternBruteForce(s: str) -> bool:
        """
            Time complexity: O(N * sqrt(N))
            Space complexity: O(1)
        """

        def pattern(n):
            for i in range(0, len(s) - n, n):
                if s[i: i + n] != s[i + n: i + 2 * n]:
                    return False
            return True

        for i in range(1, len(s) // 2 + 1):
            if pattern(i):
                return True
        return False


if __name__ == "__main__":
    print(Solution.repeatedSubstringPattern(s="ababab"))
