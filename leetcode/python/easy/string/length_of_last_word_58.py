class Solution(object):
    @staticmethod
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.strip()
        if len(res) == 0:
            return 0

        i = len(res) - 1
        count = 0

        while res[i].isalpha():
            count += 1
            i -= 1
            if i < 0:
                break

        return count
    @staticmethod
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stripped = s.strip()
        words = stripped.split(" ")
        return len(words[-1])

if __name__ == "__main__":
    print(Solution().lengthOfLastWord2(Solution, s="   fly me   to   the moon  "))