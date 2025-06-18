import collections
import itertools


class Solution:

    @staticmethod
    def largestVariance(self, s: str) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N)
        """
        max_variance = 0

        # create distinct list of character pairs
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

        # run once for original string order, then again for reverse string order
        for _ in range(2):
            for pair in pairs:
                count1 = count2 = 0
                for letter in s:
                    # no reason to process letters that aren't part of the current pair
                    if letter not in pair:
                        continue
                    if letter == pair[0]:
                        count1 += 1
                    elif letter == pair[1]:
                        count2 += 1
                    if count1 < count2:
                        count1 = count2 = 0
                    elif count1 > 0 and count2 > 0:
                        max_variance = max(max_variance, count1 - count2)

            # reverse the string for the second time around
            s = s[::-1]

        return max_variance

    @staticmethod
    def largestVarianceSecond(self, s: str) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N)
        """
        counter = collections.Counter(s)
        res = 0

        for char1, char2 in itertools.permutations(counter, 2):
            char1_count = counter[char1]
            char2_count = counter[char2]

            diff = 0

            seen_char1 = seen_char2 = False

            for char in s:
                if char not in (char1, char2):
                    continue

                if diff < 0:
                    if not char1_count:
                        break

                    if not char2_count:
                        res = max(res, diff + char1_count)
                        break
                    seen_char1 = seen_char2 = False
                    diff = 0

                if char == char1:
                    seen_char1 = True
                    char1_count -= 1
                    diff += 1

                if char == char2:
                    seen_char2 = True
                    char2_count -= 1
                    diff -= 1

                if seen_char1 and seen_char2:
                    res = max(res, diff)

        return res


if __name__ == "__main__":
    print(Solution.largestVarianceSecond(self=Solution, s="aababbb"))
