from typing import List


class Solution:

    @staticmethod
    def compress(self, chars: List[str]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        i = 0
        index = 0

        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            chars[index] = chars[i]
            index += 1

            count = j - i
            if count > 1:
                for char in str(count):
                    chars[index] = char
                    index += 1

            i = j

        # chars = chars[:index]
        return index

    @staticmethod
    def compressSecondSolution(self, chars: List[str]) -> int:
        s = ""
        curr = chars[0]
        i = 0
        while i < len(chars) - 1:
            counter = 0
            while i <= len(chars) - 1 and curr == chars[i]:
                counter += 1
                i += 1

            s += curr + str(counter) if counter > 1 else curr
            curr = chars[i] if i < len(chars) - 1 else None

        chars = list(s)
        return len(chars)


if __name__ == "__main__":
    print(Solution.compress(self=Solution, chars=["a", "a", "b", "b", "c", "c", "c"]))
