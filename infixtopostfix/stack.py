'''
coding: utf-8
Data Structure: Stack
Created 2014-09-23 23:22
ZouJingLin <zjl_717@sina.com>
'''

class Stack:
    def __init__(self):
        self.items = []

    # test whether the stack is empty
    def isEmpty(self):
        return self.items == []

    # return the numbers of items on the stack
    def size(self):
        return len(self.items)

    # return the top item from the stack but don't remove
    def peek(self):
        return self.items[len(self.items) - 1]

    # add a new item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove the top item from the stack
    def pop(self):
        return self.items.pop()
