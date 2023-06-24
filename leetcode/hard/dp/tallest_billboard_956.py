from typing import List


class Solution:
    @staticmethod
    def tallestBillboard(self, rods: List[int]) -> int:
        def diff_h(rods: list[int]) -> dict[int, int]:
            dh = {0: 0}
            for rod in rods:
                for d, h in list(dh.items()):
                    dh[d + rod] = max(dh.get(d + rod, 0), h)
                    dh[abs(d - rod)] = max(dh.get(abs(d - rod), 0), h + min(d, rod))
            return dh

        d1, d2 = diff_h(rods[: len(rods) // 2]), diff_h(rods[len(rods) // 2:])
        return max(v1 + d2[k1] + k1 for k1, v1 in d1.items() if k1 in d2)


if __name__ == "__main__":
    print(Solution.tallestBillboard(self=Solution, rods=[1, 2, 3, 4, 5, 6]))
