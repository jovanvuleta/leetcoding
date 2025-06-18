from collections import Counter


class Solution:

    @staticmethod
    def buddyStrings(self, a, b):
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        if len(a) != len(b):
            return False
        if a == b and len(set(a)) < len(a):
            return True
        res = []
        for i in range(len(a)):
            if a[i] != b[i]:
                res.append([a[i], b[i]])
            if len(res) > 2:
                return False
        return len(res) == 2 and res[0] == res[1][::-1]

    @staticmethod
    def buddyStringsSecond(self, s: str, goal: str) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        c1, c2 = Counter(s), Counter(goal)
        if c1 != c2:
            return False

        diff = sum([1 for i in range(len(s)) if s[i] != goal[i]])

        if diff == 2:
            return True
        elif diff == 0:
            return any([cnt > 1 for char, cnt in c1.items()])
        else:
            return False


if __name__ == "__main__":
    print(Solution.buddyStrings(self=Solution, a="baa", b="aab"))
    # print(Solution.buddyStrings(self=Solution, s="ba", goal="ab"))
