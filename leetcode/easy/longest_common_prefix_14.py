from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(0, len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    @staticmethod
    def solutionTwo(self, strs: List[str]):
        """
            Time complexity: O(S) where S is total number of characters in strs list
            Space complexity: O(1)
        """
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[0:-1]
        return prefix


if __name__ == "__main__":
    result = Solution.solutionTwo(self=Solution, strs=["flower", "flow", "flight"])
    print(result)
