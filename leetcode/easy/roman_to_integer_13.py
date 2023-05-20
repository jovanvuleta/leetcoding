class Solution:
    @staticmethod
    def romanToInt(self, s: str) -> int:
        """
            Solution: Go backwards through the string and see if you should add or subtract based on the number positioning.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        N = len(s)
        i = N - 1
        res = 0

        while i >= 0:
            if i < N - 1 and lookup[s[i]] < lookup[s[i + 1]]:
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
            i -= 1
        return res


if __name__ == "__main__":
    result = Solution.romanToInt(self=Solution, s="MCMXCIV")
    print(result)
