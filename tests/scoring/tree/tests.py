from unittest import TestCase
from haikuwriters.scoring.tree.ScoreTree import ScoreTree, Score, nil, Add

class TestScoreTree(TestCase):
    def test_str_nil(self):
        self.assertEqual("nil", str(nil))

    def test_str_score(self):
        self.assertEqual("1", str(ScoreTree(Score(1))))

    def test_str_add(self):
        self.assertEqual("(1 + 1)", str(ScoreTree(Add(Score(1), Score(1)))))

    def test_draw_add(self):
        actual = ScoreTree(Add(Score(1), Score(1))).draw()
        self.assertEqual("""\
+
|_ 1
|_ 1""", actual)

    def test_draw_two_levels(self):
        actual = ScoreTree(Add(Score(2), Add(Score(1), Score(1)))).draw()
        self.assertEqual("""\
+
|_ 2
|_ +
   |_ 1
   |_ 1""", actual)

    def test_equal_empty_and_nil(self):
        self.assertEqual(nil, ScoreTree())

    def test_equal_scores(self):
        self.assertEqual(Score(1), Score(1))

