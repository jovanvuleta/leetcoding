class Solution:
    @staticmethod
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
            Time complexity: O(m, n) * O(n + m)
            Space complexity: O(N)
        """
        len1, len2 = len(str1), len(str2)

        def is_divisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                return str1[:l]
        return ""


if __name__ == "__main__":
    print(Solution.gcdOfStrings(self=Solution, str1="abc", str2="efg"))
