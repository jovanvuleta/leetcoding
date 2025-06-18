from collections import deque


class RecentCounter:
    """
        Time complexity: O(N)
        Space complexity: O(N)
    """

    def __init__(self):
        self.q = deque([])
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.cnt += 1
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.cnt -= 1

            return self.cnt

        return self.cnt


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))
    print(rc.ping(100))
    print(rc.ping(3001))
    print(rc.ping(3002))
    print(rc.ping(3101))
    print(rc.ping(6102))
