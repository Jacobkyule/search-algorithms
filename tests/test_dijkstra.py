import unittest
from algorithms.dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_shortest_path(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        result = dijkstra(graph, 'A')
        self.assertEqual(result['D'], 4)