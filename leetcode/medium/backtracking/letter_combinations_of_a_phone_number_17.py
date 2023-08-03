from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            Time complexity: O(n * 4^N)
            Space complexity: O(N)
        """
        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return

            for c in digits_to_char[digits[i]]:
                backtrack(i + 1, curr_str + c)

        res = []
        digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits:
            backtrack(0, "")
        return res


if __name__ == "__main__":
    print(Solution.letterCombinations(self=Solution, digits="23"))
