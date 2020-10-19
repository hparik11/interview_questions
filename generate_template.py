# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: generate_template.py
# @Date:   9/29/20, Tue

"""
Random Sentence Generator
The goal of this exercise is to create an algorithm that can take some sentence template data, and create a randomly generated word, phrase, or an entire sentence from it.

You will need to implement the function generate_template(group_id, template_data) => str.

Template Data
To understand how to implement generate_template(...) you will need to understand how the template_data parameter is structured. Here's an example of what the template_data parameter looks like:

[
    {
        "group_id": 154,
        "children": [234, 124, 36]
    },
    {
        "group_id": 234,
        "content": "I"
    },
    {
        "group_id": 234,
        "content": "You"
    },
    {
        "group_id": 234,
        "content": "We"
    },
    {
        "group_id": 124,
        "content": "like to"
    },
    {
        "group_id": 124,
        "content": "sometimes"
    },
    {
        "group_id": 36,
        "content": "jog"
    },
    {
        "group_id": 36,
        "children": [46, 242]
    },
    {
        "group_id": 46,
        "content": "eat"
    },
    {
        "group_id": 242,
        "content": "sandwiches"
    },
    {
        "group_id": 242,
        "content": "eggs"
    }
]
Here's an image of the same template_data laid out visually in a tree:


(If that image isn't showing, you can view it here)

Note how the algorithm only chooses one template (white box) from each group (green box) as it traverses the tree to generate a sentence.

Examples
Here are some examples of Strings returned by generate_template(...) if it were given the above template_data.

generate_template(46, template_data) would return:
"eat"
generate_template(124, template_data) would return one of the following:
"like to"
"sometimes"
generate_template(36, template_data) would return one of the following:
"jog"
"eat sandwiches"
"eat eggs"
generate_template(154, template_data) would return one of the following:
"I like to jog"
"We like to eat sandwiches"
"You sometimes eat eggs"
"I sometimes eat sandwiches"
And many more possible sentences...
FAQ
So does generate_template(...) always return a full sentence?
No. Depending on the given group_id it might return a single word, a sequence of words, or a coherent sentence.
Does generate_template(...) return all possible outputs for a given group_id?
No. generate_template(...) should return only one of the possible outputs for a given template.
Are the group IDs numbered in any meaningful way?
No. The group_id for each template is randomly generated & completely arbitrary.
Hints
This is a tree-based algorithm problem, not a NLP problem.
Don't worry too much about performance, just worry about writing clean and functional code 🙂
Python has a built-in random module. random.choice(arr) might come in handy 👍
"""

import random
from collections import deque


def generate_template(group_id, template_data):
    """
    Randomly generates a string based on the given group_id & template_data
    :param group_id: int - ID for one of the groups in template_data
    :param template_data: list - List of templates (see example in description)
    :return: str - The randomly generated string based on the given group ID
    """
    templateHashMap = {}

    for each_group in template_data:
        if each_group["group_id"] not in templateHashMap:
            templateHashMap[each_group["group_id"]] = {}

        if "children" in each_group:
            if "children" in templateHashMap[each_group["group_id"]]:
                templateHashMap[each_group["group_id"]]["children"].extend(each_group['children'])
            else:
                templateHashMap[each_group["group_id"]]["children"] = each_group['children']

        if "content" in each_group:
            if "content" in templateHashMap[each_group["group_id"]]:
                templateHashMap[each_group["group_id"]]["content"].append(each_group['content'])
            else:
                templateHashMap[each_group["group_id"]]["content"] = [each_group['content']]

    if group_id not in templateHashMap:
        return ""

    # Now let's apply BFS to generate a random string
    queue = deque([group_id])
    visited = {}
    randomly_generated_string = ""

    while len(queue) > 0:
        for _ in range(len(queue)):
            child = queue.popleft()

            if 'content' in templateHashMap[child]:
                setOfContents = templateHashMap[child]['content']
                randomly_generated_string += random.choice(setOfContents) + " "
            else:
                for otherChild in traverse_template(child, templateHashMap, visited):
                    queue.append(otherChild)

    return randomly_generated_string.strip()


def traverse_template(group, templateHashMap, visited):
    """
    traverse the graph to find children.
    Args:
        group: each child group
        templateHashMap: dictionary of template
        visited: a dictionary to keep track of all visited children

    Returns:

    """
    if group in visited:
        return []
    if 'children' not in templateHashMap[group]:
        return []

    visited[group] = True

    otherChildren = list()
    allChildren = templateHashMap[group]['children']
    for child in allChildren:
        if child not in visited and child not in templateHashMap:
            continue

        otherChildren.append(child)

    return otherChildren


if __name__ == '__main__':
    print(generate_template(154, [{'group_id': 154, 'children': [234, 124, 36]}, {'group_id': 234, 'content': 'I'},
                                 {'group_id': 234, 'content': 'You'}, {'group_id': 234, 'content': 'We'},
                                 {'group_id': 124, 'content': 'like to'}, {'group_id': 124, 'content': 'sometimes'},
                                 {'group_id': 36, 'content': 'jog'}, {'group_id': 36, 'children': [46, 242]},
                                 {'group_id': 46, 'content': 'eat'}, {'group_id': 242, 'content': 'sandwiches'},
                                 {'group_id': 242, 'content': 'eggs'}]))
