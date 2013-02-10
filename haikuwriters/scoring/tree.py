from nltk.tree import ImmutableTree


class ScoreTree(ImmutableTree):
    def __str__(self):
        if self.node == None:
            return "()"
        else:
            return super().__str__()


Nil = ScoreTree(None, [])


class Score(ScoreTree):
    def __init__(self, score:int):
        self.score = score
        super().__init__(str(score), Nil)

    def __str__(self):
        return str(self.score)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.score) + ")"


class Operation(ScoreTree):
    def __init__(self, symbol:str):
        self.symbol = symbol
        super().__init__(symbol, Nil)


# class NoOp(Operation):
#     def __init__(self):
#         super().__init__("")
# NoOp = NoOp()


class Combinator(ScoreTree):
    def __init__(self, op:Operation, *children:ScoreTree):
        super().__init__(op.symbol, children)


class BinaryOperator(Combinator):
    def __init__(self, left:ScoreTree, right:ScoreTree):
        self.left = left
        self.right = right
        super().__init__(self.operation, left, right)

    def __str__(self):
        return "(" + str(self.left) + " " + self.operation.symbol + " " + str(self.right) + ")"


class Add(BinaryOperator):
    operation = Operation("+")
    # def __init__(self, left:ScoreTree, right:ScoreTree):
    #     super().__init__(Add.operation, left, right)


class Multiply(BinaryOperator):
    operation = Operation("*")
    # def __init__(self, left:ScoreTree, right:ScoreTree):
    #     super().__init__(Multiply.operation, left, right)
