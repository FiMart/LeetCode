class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(set)

        # Build the graph and map emails to names
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                graph[account[1]].add(email)
                graph[email].add(account[1])

        visited = set()
        merged_accounts = []

        # DFS to find all connected components
        def dfs(email):
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return component

        for email in email_to_name.keys():
            if email not in visited:
                component = dfs(email)
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts