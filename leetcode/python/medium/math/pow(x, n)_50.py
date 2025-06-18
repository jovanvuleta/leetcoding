class Solution:
    @staticmethod
    def myPow(self, x: float, n: int) -> float:
        """
            Time complexity: O(log(2**n))
            Space complexity: O(N)
        """

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res


if __name__ == "__main__":
    print(Solution.myPow(self=Solution, x=2.0, n=10))
