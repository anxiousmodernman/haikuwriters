from unittest import TestCase
from haikuwriters.scoring.tree import ScoreTree, Score, Nil, Add, Multiply


class TestScoreTree(TestCase):
    def test_str_nil(self):
        self.assertEqual("()", str(Nil))

    def test_str_nil_equals_empty(self):
        self.assertEqual(str(ScoreTree(None, ())), str(Nil))

    def test_str_score(self):
        self.assertEqual("1", str(Score(1)))

    def test_str_add(self):
        self.assertEqual("(1 + 1)", str(Add(Score(1), Score(1))))

    def test_str_multiply(self):
        self.assertEqual("(1 * 1)", str(Multiply(Score(1), Score(1))))

    def test_str_nested(self):
        self.assertEqual("(1 * (2 + 3))", str(Multiply(Score(1), Add(Score(2), Score(3)))))

    def test_equal_empty_and_nil(self):
        self.assertEqual(Nil, ScoreTree(None, ()))

    def test_equal_scores(self):
        self.assertEqual(Score(1), Score(1))

