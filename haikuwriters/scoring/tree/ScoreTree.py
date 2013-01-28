class Node:
    _left = None
    _right = None

    def __init__(self, data):
        self.data = data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __eq__(self, other):
        if other.data is None and self.data is None:
            return True
        elif other.data != self.data:
            return False
        elif (other.left != self.left and
            other.right != self.right):
            return False
        else:
            return True

    def draw(self, level:int):
        if self.data is None:
            return "empty"
        else:

            builder = str(self.data)
            branch = "\n" + ("   " * level) + "|_ "
            level += 1
            if self.left is not None:
                builder += branch + self.left.draw(level)
            if self.right is not None:
                builder += branch + self.right.draw(level)
            return builder

    def __str__(self):
        return "nil"

    def __repr__(self):
        return empty

empty = Node(None)

class Score(Node):
    def __init__(self, score:int):
        super().__init__(score)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)


class Combinator(Node):
    def __init__(self, op:str, left:Node, right:Node):
        super().__init__(op)
        self._left = left
        self._right = right

    def __str__(self):
        builder = "("
        if self.left is not None:
            builder += str(self.left)
        builder += " " + self.data + " "
        if self.right is not None:
            builder += str(self.right)
        builder += ")"
        return builder

    def __repr__(self):
        builder = self.__class__.__name__ + "("
        if self.left is not None:
            builder += repr(self.left)
        builder += ", "
        if self.right is not None:
            builder += repr(self.right)
        builder += ")"
        return builder

class Add(Combinator):
    def __init__(self, left:Node, right:Node):
        super().__init__("+", left, right)


class ScoreTree:
    def __init__(self, root:Node=empty):
        self.root = root

    def draw(self):
        return self.root.draw(0)

    def __eq__(self, other):
        return self.root == other.root

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return repr(self.root)

nil = ScoreTree()