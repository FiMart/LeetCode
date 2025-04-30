class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count('R')
        d_count = senate.count('D')
        r_ban = 0
        d_ban = 0

        while r_count > 0 and d_count > 0:
            for i in range(len(senate)):
                if senate[i] == 'R':
                    if r_ban > 0:
                        r_ban -= 1
                        r_count -= 1
                        senate = senate[:i] + 'X' + senate[i + 1:]
                    else:
                        d_ban += 1
                elif senate[i] == 'D':
                    if d_ban > 0:
                        d_ban -= 1
                        d_count -= 1
                        senate = senate[:i] + 'X' + senate[i + 1:]
                    else:
                        r_ban += 1

        return "Radiant" if r_count > 0 else "Dire"