class Solution:
    @staticmethod
    def isValid(self, s: str) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        stack = []
        for char in s:
            if char in [")", "}", "]"]:
                if len(stack) == 0:
                    return False
                elif stack[-1] == "{" and char == "}"\
                        or stack[-1] == "[" and char == "]"\
                        or stack[-1] == "(" and char == ")":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution.isValid(self=Solution, s="(])"))
