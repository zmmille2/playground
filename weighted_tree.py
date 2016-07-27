from sets import Set

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, Node):
        self.children.append(Node)

    def is_leaf(self):
        return len(self.children) == 0
    
    # returns a list of the max values this node could store.
    def possible_capacities(self):
        if self.is_leaf():
            return Set([self.value])

        possible_values = Set()
        pass

class innerNode(Node):
    def __init__(self, capacity):
        self.capacity = capacity
        self.children = []

    def add_child(self, Node):
        self.children.append(Node)
    pass

class Leaf(Node):
    def __init__(self, weight):
        self.weight = weight
    pass

class Tree:
    def __init__(self, root):
        self.root = root

    def possible_capacities():
        return root.possible_capacities()[0]
    pass
