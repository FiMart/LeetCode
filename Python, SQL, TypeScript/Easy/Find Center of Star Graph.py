class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center of a star graph is the common node in the two edges.
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]