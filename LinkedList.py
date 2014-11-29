__author__ = 'kasper'

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Podredena
class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def length(self):
        return self.length

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def ins(self, node):
        if not self.head:
            self.head = node
            self.length += 1
            return 1

        return 0
