class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]  # (snap_id, value)
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_count, val))

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_arr = self.arr[index]
        low, high = 0, len(snap_arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if snap_arr[mid][0] <= snap_id:
                low = mid + 1
            else:
                high = mid - 1

        return snap_arr[high][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

if __name__ == "__main__":
    obj = SnapshotArray(1)
    obj.set(0, 15)
    param_2 = obj.snap()
    param_3 = obj.snap()
    param_4 = obj.snap()
    param_5 = obj.get(0, 2)
    param_6 = obj.snap()
    param_7 = obj.snap()
    param_8 = obj.get(0, 0)
    print('done')
