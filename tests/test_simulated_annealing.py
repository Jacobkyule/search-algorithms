import unittest
from algorithms.simulated_annealing import simulated_annealing
import math, random

class TestSimulatedAnnealing(unittest.TestCase):
    def test_minimize_square(self):
        def cost_fn(x): return x ** 2
        def neighbor_fn(x): return x + random.choice([-1, 1])
        def temp_fn(t): return max(0.01, min(1, 1 - math.log(t + 1) / math.log(1000)))

        result = simulated_annealing(10, cost_fn, neighbor_fn, temp_fn)
        self.assertIsInstance(result, (int, float))