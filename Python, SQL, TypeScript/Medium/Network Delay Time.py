class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        total_time = 0

        while min_heap:
            time, node = heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_time = max(total_time, time)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heappush(min_heap, (time + weight, neighbor))

        return total_time if len(visited) == n else -1