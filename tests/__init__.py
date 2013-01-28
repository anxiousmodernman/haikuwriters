from unittest import TestCase
from haikuwriters.scoring.tree.ScoreTree import ScoreTree

class TestScoreTreeSerializer(TestCase):

    def test_empty_tree(self):
        self.assertEqual(str(ScoreTree()), "()")
