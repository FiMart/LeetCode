class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)

        def dfs(index, sides):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == side
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1, sides):
                        return True
                    sides[i] -= matchsticks[index]
            return False

        return dfs(0, [0] * 4)