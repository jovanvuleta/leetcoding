class Solution:
    @staticmethod
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
            Time complexity: O(max(len(word1), len(word2))
            Space complexity: O(max(len(word1), len(word2))
        """
        zip_list = zip(word1, word2)
        res = ''.join(x[0] + x[1] for x in zip_list)
        res += word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):]
        return res

    @staticmethod
    def mergeAlternatelyPointerSolution(self, word1: str, word2: str) -> str:
        """
            Time complexity: O(min(len(word1), len(word2))
            Space complexity: O(1) - just the return string but we are not counting that
        """
        i = 0
        res = ""

        while i < len(word1) and i < len(word2):
            res += word1[i] + word2[i]
            i += 1

        res += word1[i:] if len(word1) > len(word2) else word2[i:]

        return res


if __name__ == "__main__":
    print(Solution.mergeAlternately(self=Solution, word1="abc", word2="efg"))
    print(Solution.mergeAlternatelyPointerSolution(self=Solution, word1="abc", word2="efg"))
