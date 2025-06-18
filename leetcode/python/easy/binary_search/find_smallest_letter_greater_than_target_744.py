from typing import List


class Solution:
    @staticmethod
    def nextGreatestLetter(letters: List[str], target: str) -> str:
        res = letters[0]

        l, r = 0, len(letters) - 1

        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) < ord(target):
                l = mid + 1
            elif ord(letters[mid]) == ord(target):
                l = mid + 1
            else:
                res = letters[mid]
                r = mid - 1

        return res


if __name__ == "__main__":
    print(Solution.nextGreatestLetter(letters=["a", "b", "x", "y", "y"], target="a"))
