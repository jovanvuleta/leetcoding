class Solution:
    @staticmethod
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
            Time complexity: O(log(maxSum) * log(n))
            Space complexity: O(1)
        """

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

    @staticmethod
    def maxValueSecondSolution(self, n: int, index: int, maxSum: int) -> int:
        res = 1
        left, right = 0, maxSum

        def sequence(attempt):
            total = 0
            # can fit sequence on left side
            if index + 1 >= attempt:
                total += attempt * (attempt + 1) // 2
                left_of_sequence = index - attempt
                total += left_of_sequence + 1
            # can't fit sequence on left side
            else:
                total += attempt * (attempt + 1) // 2
                left_of_sequence = attempt - (index + 1)
                total -= left_of_sequence * (left_of_sequence + 1) // 2

            end = n - 1
            # can fit sequence on right side
            if(end - index + 1) >= attempt:
                total += attempt * (attempt + 1) // 2
                right_of_sequence = index + attempt
                total += end - right_of_sequence + 1
            # can't fit sequence on right side
            else:
                total += attempt * (attempt + 1) // 2
                right_of_sequence = attempt - (end + 1 - index)
                total -= right_of_sequence * (right_of_sequence + 1) // 2

            total -= attempt
            return total

        while left <= right:
            mid = (left + right) // 2
            if sequence(mid) <= maxSum:
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == "__main__":
    print(Solution.maxValue(self=Solution, n=4, index=2, maxSum=6))
