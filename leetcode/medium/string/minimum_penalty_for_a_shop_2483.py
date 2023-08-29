class Solution:
    @staticmethod
    def bestClosingTime(customers: str) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        n = len(customers)

        y = 0

        for i in range(n):
            y += (1 if customers[i] == "Y" else 0)

        min_penalty = n
        hour = n

        y_found = 0
        n_found = 0

        for h in range(n + 1):
            y_remaining = y - y_found

            penalty = y_remaining + n_found

            if penalty < min_penalty:
                hour = h
                min_penalty = penalty

            n_found += (1 if h < n and customers[h] == "N" else 0)
            y_found += (1 if h < n and customers[h] == "Y" else 0)

        return hour


if __name__ == "__main__":
    print(Solution.bestClosingTime(customers="YYNY"))
