class Solution:
    @staticmethod
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
            Time complexity: O(M * N)
            Space complexity: O(M * N)
        """
        cache = {}

        def helper(i, j):
            """return the minimum ASCII sum for s1[i:] and s2[j:]"""
            if i >= len(s1):
                return sum([ord(x) for x in s2[j:]])

            if j >= len(s2):
                return sum([ord(x) for x in s1[i:]])

            if (i, j) not in cache:
                if s1[i] == s2[j]:
                    cache[(i, j)] = helper(i + 1, j + 1)
                else:
                    cache[(i, j)] = min(helper(i + 1, j) + ord(s1[i]), helper(i, j + 1) + ord(s2[j]))
            return cache[(i, j)]

        return helper(0, 0)


if __name__ == "__main__":
    print(Solution.minimumDeleteSum(self=Solution, s1="delete", s2="leet"))
