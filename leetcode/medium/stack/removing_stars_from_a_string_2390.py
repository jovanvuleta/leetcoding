class Solution:
    @staticmethod
    def removeStars(self, s: str) -> str:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        stack = []

        for ch in s:
            if ch != "*":
                stack.append(ch)
                continue
            stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    print(Solution.removeStars(self=Solution, s="abb*cdfg*****x*"))
