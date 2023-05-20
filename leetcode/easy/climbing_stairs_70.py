class Solution:
    @staticmethod
    def climbStairs(self, n: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


if __name__ == "__main__":
    print(Solution.climbStairs(self=Solution, n=3))
