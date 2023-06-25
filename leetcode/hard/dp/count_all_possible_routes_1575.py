from typing import List


class Solution:
    MOD = 1000000007

    def helper(self, locations, city, finish, remainFuel, memo):
        if remainFuel < 0:
            return 0

        if memo[city][remainFuel] is not None:
            return memo[city][remainFuel]

        total = 1 if city == finish else 0

        for nextCity in range(len(locations)):
            if nextCity != city and remainFuel >= abs(locations[nextCity] - locations[city]):
                total = (total + self.helper(locations, nextCity, finish,
                                             remainFuel - abs(locations[nextCity] - locations[city]), memo)) % self.MOD

        memo[city][remainFuel] = total
        return total

    @staticmethod
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        memo = [[None] * (fuel + 1) for _ in range(n)]
        return self.helper(locations, start, finish, fuel, memo)


if __name__ == "__main__":
    print(Solution.countRoutes(self=Solution, locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))
