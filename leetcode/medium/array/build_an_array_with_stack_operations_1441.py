from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        initialValue = 1
        output = []
        for number in target:
            output.extend(["Push","Pop"]*(number - initialValue) + ["Push"])
            initialValue = number + 1
        return output
