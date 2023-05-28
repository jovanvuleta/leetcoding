class Solution:
    @staticmethod
    def reverseVowels(self, s: str) -> str:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        start = 0
        end = len(s) - 1

        s_list = list(s)

        while start <= end:
            if s[start] in vowels and s[end] in vowels:
                s_list[start], s_list[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] not in vowels:
                start += 1
            else:
                end -= 1

        return "".join(s_list)


if __name__ == "__main__":
    print(Solution.reverseVowels(self=Solution, s="hEllo"))
