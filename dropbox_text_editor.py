#!/usr/bin/env python
# coding:utf-8
"""
@FileName : dropbox_text_editor.py
@Author   : Harsh Parikh
@Date     : 7/13/21 12:47 AM

Implement Text Editor Undo Redo
We aim to implement rudimentary undo & redo.

You will be provided a set of actions to perform. Once all actions are performed you will return the current state the system should be in after all actions in actions are performed.

We will be operating on characters and the "state" of the system will be a string that we are building.

These are the actions possible:
INSERT: Inserts a single character to the end of the string
DELETE: Removes the last character in the string
UNDO: Reverses the most recent action
REDO: Redoes the most recent action undone

Your inputs will only be single characters. There are only 4 input actions as enumerated above.

Example 1:
Input:
INSERT 'a'
INSERT 'b'

Output: "ab"

Example 2:
Input:
INSERT 'a'
INSERT 'b'
UNDO

Output: "a"

Example 3:
Input:
INSERT 'a'
INSERT 'b'
UNDO
REDO

Output: "ab"

Example 4:
Input:
INSERT 'a'
INSERT 'b'
UNDO
REDO
REDO # Does nothing

Output: "ab"
"""

from copy import deepcopy


class TextEditor:

    def __init__(self):
        self.text = []
        self.undo_ops = []
        self.redo_ops = []
        self.clipboard = []

    def __repr__(self):
        return ''.join(self.text)

    def insert(self, text):
        if text:
            self.undo_ops.append(deepcopy(self.text))
            self.text += list(text)

    def delete(self):
        if self.text:
            self.undo_ops.append(deepcopy(self.text))
            self.text.pop()

    def copy(self, index):
        if index < len(self.text):
            self.clipboard = deepcopy(self.text[index:])

    def paste(self):
        if self.clipboard:
            self.undo_ops.append(deepcopy(self.text))
            self.text += deepcopy(self.clipboard)

    def undo(self):
        if self.undo_ops:
            self.redo_ops.append(deepcopy(self.text))
            self.text = self.undo_ops.pop()

    def redo(self):
        if self.redo_ops:
            self.undo_ops.append(deepcopy(self.text))
            self.text = self.redo_ops.pop()

    def bold(self, i, j):
        if self.text:
            self.undo_ops.append(deepcopy(self.text))
            self.text.insert(j + 1, '*')
            self.text.insert(i, '*')


if __name__ == '__main__':
    textEditor = TextEditor()
    textEditor.insert("a")
    print("1st:", textEditor)
    textEditor.insert("b")
    print("2nd:", textEditor)
    textEditor.insert("c")
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.delete()
    print("3rd:", textEditor)
    textEditor.undo()
    print("7th:", textEditor)
    textEditor.undo()
    print("7th:", textEditor)
    textEditor.undo()
    print("7th:", textEditor)
    textEditor.undo()
    print("7th:", textEditor)
    textEditor.copy(0)
    print("4th:", textEditor)
    textEditor.paste()
    print("5th:", textEditor)
    textEditor.insert("m")
    print("6th:", textEditor)
    textEditor.bold(2, 4)
    print(textEditor)
    # textEditor.undo()
    # print("7th:", textEditor)
    # textEditor.undo()
    # print("7th:", textEditor)
    # textEditor.redo()
    # print("8th:", textEditor)
    # textEditor.undo()
    # print("9th:", textEditor)
    # textEditor.undo()
    # print("9th:", textEditor)
    # textEditor.redo()
    # print("10th:", textEditor)
    # textEditor.redo()
    # print("10th:", textEditor)

    #####################################################

    # textEditor1 = TextEditor()
    # textEditor1.insert("Da")
    # print("1st:", textEditor1)
    # textEditor1.copy(0)
    # print("4th:", textEditor1)
    # textEditor1.undo()
    # print("7th:", textEditor1)
    # textEditor1.paste()
    # print("5th:", textEditor1)
    # textEditor1.paste()
    # print("5th:", textEditor1)
    # textEditor1.copy(2)
    # print("4th:", textEditor1)
    # textEditor1.paste()
    # print("5th:", textEditor1)
    # textEditor1.paste()
    # print("5th:", textEditor1)
    # textEditor1.delete()
    # print("3rd:", textEditor1)
    # textEditor1.insert("aaam")
    # print("2nd:", textEditor1)
