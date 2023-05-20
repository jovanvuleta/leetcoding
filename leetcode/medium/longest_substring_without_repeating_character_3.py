class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
            Solution: Sliding window technique, where you move the i pointer until you find a existing character in the
            set, then you move the end pointer and remove all the chars from the set until you remove a duplicate char
            from the set, then continue forward with the pointer.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        char_set = set()
        end = 0
        counter = 0

        for i in range(0, len(s)):
            while s[i] in char_set:
                char_set.remove(s[end])
                end += 1

            char_set.add(s[i])
            counter = max(counter, i - end + 1)

        return counter


if __name__ == "__main__":
    result = Solution.lengthOfLongestSubstring(s="abcabcbb")
    print(result)
