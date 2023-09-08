from typing import List


class Solution:
    @staticmethod
    def generate(self, numRows: int) -> List[List[int]]:
        """
            Time complexity: O(N^2) - N number of rows
            Space complexity: O(N^2)
        """
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

    @staticmethod
    def generateSecondSolution(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for r in range(2, numRows + 1):
            tmp = [1]
            for c in range(1, r - 1):
                tmp.append(output[-1][c] + output[-1][c - 1])
            tmp.append(1)
            output.append(tmp)

        return output


if __name__ == "__main__":
    print(Solution.generate(self=Solution, numRows=5))
