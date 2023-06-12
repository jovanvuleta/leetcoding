from collections import Counter


class Solution:
    @staticmethod
    def closeStrings(word1: str, word2: str) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        count1 = Counter(word1)
        count2 = Counter(word2)

        return Counter(count1.values()) == Counter(count2.values()) and set(count1.keys()) == set(count2.keys())

    """
    cabbba -> caabbb -> baaccc -> abbccc
    """


if __name__ == "__main__":
    print(Solution.closeStrings(word1="cabbba", word2="abbccc"))
    # print(Solution.closeStrings(word1="abbzzca", word2="babzzcz"))
