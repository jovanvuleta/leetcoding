class Solution:
    @staticmethod
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(a):
            left_offset = max(a - index, 0)
            result = (a + left_offset) * (a - left_offset + 1) // 2
            right_offset = max(a - ((n - 1) - index), 0)
            result += (a + right_offset) * (a - right_offset + 1) // 2
            return result - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1


if __name__ == "__main__":
    print(Solution.maxValue(self=Solution, n=4, index=2, maxSum=6))
