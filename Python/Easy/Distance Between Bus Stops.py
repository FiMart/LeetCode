class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        start, destination = min(start, destination), max(start, destination)
        clockwise_distance = sum(distance[start:destination])
        counter_clockwise_distance = sum(distance) - clockwise_distance
        return min(clockwise_distance, counter_clockwise_distance)