class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {
            1: {"size": big, "count": 0},
            2: {"size": medium, "count": 0},
            3: {"size": small, "count": 0},
        }

    def addCar(self, carType: int) -> bool:
        if self.slots[carType]["count"] < self.slots[carType]["size"]:
            self.slots[carType]["count"] += 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
