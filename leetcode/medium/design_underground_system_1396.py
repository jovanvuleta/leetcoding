from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        # customer_id: (start_time, station_name)
        self.i = defaultdict(tuple)
        # (source, destination): [end_time - start_time]
        self.o = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, source = self.i[id]
        self.o[(source, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[startStation, endStation]) / len(self.o[startStation, endStation])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
