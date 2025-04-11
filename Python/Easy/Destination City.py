class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set(path[0] for path in paths)
        for path in paths:
            if path[1] not in start_cities:
                return path[1]
        return ""