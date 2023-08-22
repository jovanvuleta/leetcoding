class Solution:
    def convertToTitle(columnNumber: int) -> str:
        """
            Time complexity: O(columnNumber)
            Space complexity: O(1)
        """
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while columnNumber:
            columnNumber = columnNumber - 1
            ans = abc[columnNumber % 26] + ans
            columnNumber = columnNumber // 26
        return ans

    def convertToTitleSecond(columnNumber: int) -> str:
        output = ""

        while columnNumber > 0:
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26

        return output


if __name__ == "__main__":
    print(Solution.convertToTitle(columnNumber=701))
