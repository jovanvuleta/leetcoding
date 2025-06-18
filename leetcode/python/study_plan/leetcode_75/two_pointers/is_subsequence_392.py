class Solution:
    @staticmethod
    def isSubsequence(self, s: str, t: str) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        if len(s) == 0:
            return True

        j = 0

        for i in range(0, len(t)):
            if j == len(s):
                return True
            if s[j] == t[i]:
                j += 1

        return j == len(s)

    def isSubsequenceSecond(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


if __name__ == "__main__":
    print(Solution.isSubsequence(self=Solution, s="abc", t="ahbgdc"))
