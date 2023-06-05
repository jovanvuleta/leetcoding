from typing import List


class Solution:
    @staticmethod
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        i = 0

        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]

        x_diff = x2 - x1
        y_diff = y2 - y1

        for i in range(2, len(coordinates)):
            curr_x, curr_y = coordinates[i]
            prev_x, prev_y = coordinates[i - 1]
            curr_diff_x = curr_x - prev_x
            curr_diff_y = curr_y - prev_y

            if y_diff * curr_diff_x != curr_diff_y * x_diff:
                return False

        return True


if __name__ == "__main__":
    print(Solution.checkStraightLine(self=Solution, coordinates=[[0, 0], [0, 1], [0, -1]]))
