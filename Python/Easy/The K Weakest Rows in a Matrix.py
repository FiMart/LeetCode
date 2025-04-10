class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Count the number of soldiers in each row and store the index
        soldier_counts = [(sum(row), i) for i, row in enumerate(mat)]
        # Sort by number of soldiers, then by index
        soldier_counts.sort(key=lambda x: (x[0], x[1]))
        # Extract the indices of the k weakest rows
        return [soldier_counts[i][1] for i in range(k)]