from haikuwriters.scoring.tree import ScoreTree, ScoreTerm


class Operation:
    operator = None
    def draw(self, *operands:ScoreTree):
        return type(self).__name__ + str(tuple(operands))


class Combinator(ScoreTree):
    def __init__(self, op:Operation, *children:ScoreTree):
        super().__init__(str(op), children)

    def __str__(self):
        return "(" + self.operation.draw(self.left, self.right) + ")"


class BinaryOperation(Combinator):
    def __init__(self, left:ScoreTree, right:ScoreTree):
        self.left = left
        self.right = right
        super().__init__(self.operation, left, right)


class Operator:
    def apply(self, *operands:ScoreTree):
        pass

    def draw(self, *operands:ScoreTree):
        pass


class InfixOperator(Operator):
    def __init__(self, symbol:str, apply:callable):
        self.symbol = symbol
        self.apply = apply

    def __str__(self):
        return self.symbol

    def draw(self, left:ScoreTree, right:ScoreTree):
        return str(left) + " " + str(self) + " " + str(right)


class Choose(Operator):
    def draw(self, left:ScoreTerm, right:ScoreTerm):
        return str(left.tree) + "[" + left.meta + "%] / " + str(right.tree) + "[" + right.meta + "%]"


class Add(BinaryOperation):
    operation = InfixOperator("+", lambda x, y: x + y)


class Multiply(BinaryOperation):
    operation = InfixOperator("*", lambda x, y: x * y)
