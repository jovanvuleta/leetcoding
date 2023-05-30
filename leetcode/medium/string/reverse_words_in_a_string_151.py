class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        """
            Time complexity: O(n + m) - n == len of string, m == num of words in a string
            Space complexity: O(n + m) - n == len of string, m == num of words in a string
        """
        a = s.split()[::-1]
        return " ".join(a)
