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


class ScoreTerm(ScoreTree):
    def __init__(self, meta, tree:ScoreTree):
        self.meta = meta
        super().__init__(meta, tuple(tree))

    def __str__(self):
        return "(" + self.operation.draw(self.left, self.right) + ")"

