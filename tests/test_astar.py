import unittest
from algorithms.astar import astar

class TestAStar(unittest.TestCase):
    def test_path(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        positions = {
            'A': (0, 0),
            'B': (1, 0),
            'C': (1, 1),
            'D': (2, 2)
        }
        path = astar(graph, 'A', 'D', positions)
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'D')