# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: accounts_merge.py
# @Date:   9/10/20, Thu
"""
721. Accounts Merge

Share
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email
that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people
 as people could have the same name. A person can have any number of accounts initially, but all of their accounts
 definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name,
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
"""

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        email_to_name = {}
        email_graph = defaultdict(set)

        for acc in accounts:
            name = acc[0]

            # making a graph of common connected gmail
            # all acc the gmail start with 1 index
            for email in acc[1:]:
                # connect 1st to 2nd email
                email_graph[acc[1]].add(email)

                # connect other email to 1st email
                email_graph[email].add(acc[1])

                # create a hashmap
                # it help us to find the email owners
                email_to_name[email] = name

        seen = set()
        ans = []

        # here we use loop to traverse all unconnected
        # components of the graph
        for email in email_graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []

                # this loop give us the all connected path as here
                # all common gmail as a list in component
                while stack:
                    edge = stack.pop()
                    component.append(edge)
                    for nei in email_graph[edge]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)

                # after getting all connect component
                # we sorted the as question
                # and search the owner of the starting email
                # append in the ans
                ans.append([email_to_name[email]] + sorted(component))
        return ans


class UF:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution2:
    # 196 ms, 82.09%.
    def accountsMerge(self, accounts):
        uf = UF(len(accounts))

        # Creat unions between indexes
        ownership = {}
        idxToName = {}
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
            idxToName[i] = name

        # Append emails to correct index
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[idxToName[i]] + sorted(emails) for i, emails in ans.items()]


if __name__ == '__main__':
    s = Solution()
    print(s.accountsMerge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
