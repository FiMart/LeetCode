class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {s: i for i, s in enumerate(list2)}
        ans = []
        mi = inf
        for i, s in enumerate(list1):
            if s in d:
                if i + d[s] < mi:
                    mi = i + d[s]
                    ans = [s]
                elif i + d[s] == mi:
                    ans.append(s)
        return ans