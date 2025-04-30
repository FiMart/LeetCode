class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        h = 0
        for house in houses:
            while h < len(heaters) - 1 and abs(house - heaters[h]) >= abs(house - heaters[h + 1]):
                h += 1
            radius = max(radius, abs(house - heaters[h]))
        return radius