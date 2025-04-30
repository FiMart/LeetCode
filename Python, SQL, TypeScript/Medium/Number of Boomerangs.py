class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)):
            distances = {}
            for j in range(len(points)):
                if i != j:
                    dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    distances[dist] = distances.get(dist, 0) + 1
            for k in distances.values():
                count += k * (k - 1)
        return count