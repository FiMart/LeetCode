class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)
        ans = 0
        for i in range(n):
            if initialEnergy <= energy[i]:
                ans += energy[i] - initialEnergy + 1
                initialEnergy = energy[i] + 1
            if initialExperience <= experience[i]:
                ans += experience[i] - initialExperience + 1
                initialExperience = experience[i] + 1
            initialEnergy -= energy[i]
            initialExperience += experience[i]
        return ans