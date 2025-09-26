class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        email_to_name = {}
        graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                email_to_name[email] = name

        visited = set()
        merged_accounts = []

        def dfs(email, emails):
            if email in visited:
                return
            visited.add(email)
            emails.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, emails)

        for email in graph:
            if email not in visited:
                emails = []
                dfs(email, emails)
                merged_accounts.append([email_to_name[email]] + sorted(emails))

        return merged_accounts