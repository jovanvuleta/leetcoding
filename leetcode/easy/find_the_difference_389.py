class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
            Time complexity: O(len(t) * len(s))
            Space complexity: O(len(s))
        """
        for i in t:
            if i not in s:
                return i
            s = s.replace(i, "", 1)


if __name__ == "__main__":
    print(Solution.findTheDifference(self=Solution, s="abcd", t="abcde"))
