#!/usr/bin/env python
# coding:utf-8
"""
@FileName : snapchat_chain_of_invitees.py
@Author   : Harsh Parikh
@Date     : 7/8/21 10:51 PM

PersonA -invited-> PersonB

// Mingtao,Kendyl
// Kendyl,Hamza
// Kendyl,Dayana
// Dayana,Miya
// Dayana,Kian
// Dorian,Brendan
// Dorian,Brooks
// Amari,Mckinley
// Amari,Yandel
// Yandel,Adalyn
// Yandel,Ariella
// Hamza,Terry
// Hamza,Dorian
// Terry,Abby
// -------
Example 1:
// input:
Mingtao, Kian
// output:
Mingtao invited Kendyl
Kendyl invited Dayana
Dayana invited Kian

// Example 2
//input:
Brooks, Kian
// output:
 Brooks was invited by Dorian
 Dorian was invited by Hamza
Hamza was invited by Kendyl
Kendyl invited Dayana
Dayana invited Kian

//This is the way the input is provided to your function:
people inviter -> invitees

{"mingtao" -> ("kendyl"), "kendyl" -> ("Hamza", "dayana"), "dayana" -> ("miya", "kian")}
"""

import collections


def trace_invitees(relations, start, end):
    g = collections.defaultdict(list)

    for invitee, invited in relations:
        g[invitee].append((invited, 'invited'))  # forward edge
        g[invited].append((invitee, 'was invited by'))  # backward edge

    if start not in g or end not in g:
        print('Data not found in invitees list')
        return

    visited = set()

    def dfs(start, path=''):
        if start == end:
            print(path)
            return

        if start in visited:
            return

        visited.add(start)
        for person, type in g[start]:
            relation = '%s %s %s\n' % (start, type, person)
            dfs(person, path + relation)

    dfs(start)


relations = '''
Mingtao,Kendyl
Kendyl,Hamza
Kendyl,Dayana
Dayana,Miya
Dayana,Kian
Dorian,Brendan
Dorian,Brooks
Amari,Mckinley
Amari,Yandel
Yandel,Adalyn
Yandel,Ariella
Hamza,Terry
Hamza,Dorian
Terry,Abby
'''
trimmed_data = [x.strip().split(',') for x in relations.split()]
print('\n***** Test case 1 *****')
trace_invitees(trimmed_data, 'Brooks', 'Kian')
print('\n***** Test case 2 *****')
trace_invitees(trimmed_data, 'Ariella', 'Amari')
