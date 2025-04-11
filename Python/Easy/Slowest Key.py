class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        mx = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] > mx or (releaseTimes[i] - releaseTimes[i - 1] == mx and keysPressed[i] > ans):
                mx = releaseTimes[i] - releaseTimes[i - 1]
                ans = keysPressed[i]
        return ans