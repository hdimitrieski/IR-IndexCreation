__author__ = 'kasper'

class Tree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insertLeft(self, node):
        self.left = node

    def insertRight(self, node):
        self.right = node

def printTree(tree):
        if tree == None:
            return
        print tree.value
        printTree(tree.left)
        printTree(tree.right)

def getWord(input):
    if getOper(input, '('):
        subTree = buildOrTree(input)
        getOper(input, ')')
        return subTree
    else:
        ch = input[0]
        if ch =='AND' or ch == 'OR':
            return None
        input[0:1] = []
        return Tree(ch)

def getOper(input, op):
    if len(input) > 0 and input[0] == op:
        del input[0]
        return True
    return False

def buildAndTree(input):
    lnode = getWord(input)
    if getOper(input, 'AND'):
        rnode = buildAndTree(input)
        return Tree('AND', lnode, rnode)
    else:
        return lnode

def buildOrTree(input):
    lnode = buildAndTree(input)
    if getOper(input, 'OR'):
        rnode = buildOrTree(input)
        return Tree('OR', lnode, rnode)
    else:
        return lnode
