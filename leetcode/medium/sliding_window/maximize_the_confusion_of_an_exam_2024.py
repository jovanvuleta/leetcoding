class Solution:
    @staticmethod
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l = r = 0
        d = {'T': 0, 'F': 0}
        mx = float('-inf')

        while r < len(answerKey):
            d[answerKey[r]] += 1

            while min(d['T'], d['F']) > k:
                d[answerKey[l]] -= 1
                l += 1

            mx = max(mx, r - l + 1)
            r += 1

        return mx

    @staticmethod
    def maxConsecutiveAnswersSecond(self, answerKey: str, k: int) -> int:
        res, l = 0, 0
        count = {"T": 0, "F": 0}

        for r in range(len(answerKey)):
            count[answerKey[r]] += 1

            if (r - l + 1) - max(count.values()) > k:
                count[answerKey[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    print(Solution.maxConsecutiveAnswers(self=Solution, answerKey="FFFTTFTTFT", k=1))
