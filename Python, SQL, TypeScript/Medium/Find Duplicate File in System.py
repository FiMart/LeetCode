class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for path in paths:
            path = path.split()
            for i in range(1, len(path)):
                file = path[i]
                name = file.split('(')[0]
                content = file.split('(')[1][:-1]
                ans[content].append(path[0] + '/' + name)
        return [x for x in ans.values() if len(x) > 1]