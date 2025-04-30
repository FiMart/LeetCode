class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist_sq(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        dists = [
            dist_sq(p1, p2),
            dist_sq(p1, p3),
            dist_sq(p1, p4),
            dist_sq(p2, p3),
            dist_sq(p2, p4),
            dist_sq(p3, p4)
        ]

        dists.sort()
        return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]