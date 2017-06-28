class Node():
    def __init__(self, value = 0):
        self.left = Node()
        self.right = Node()
        self.value = value

    def get_rightmost_left_child(self):
        prev, child = self, self.left
        while child.right != None:
            prev, child = child, child.right
        prev.right = child.left
        return child

    def delete(self):
        if self.left == None and self.right == None:
            self = None
        elif self.left == None:
            self = self.left
        elif self.right == None:
            self = self.right
        else:
            left, right = self.left, self.right
            self = self.get_rightmost_left_child()
            self = left, right

    def insert(self, value):
        if self.value < value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif self.value > value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def remove(self, value):
        if self.value == value:
            self.delete()
        elif self.value < value and self.left != None:
            self.left.remove(value)
        elif self.value > value and self.right != None:
            self.right.remove(value)
