class Solution:
    @staticmethod
    def maxVowels(self, s: str, k: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        vowels = {"a", "e", "i", "o", "u"}
        count = sum(1 for char in s[:k] if char in vowels)
        max_count = count

        for r in range(k, len(s)):
            if s[r - k] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            max_count = max(max_count, count)

        return max_count


if __name__ == "__main__":
    print(Solution.maxVowels(self=Solution, s="abciiidef", k=3))
