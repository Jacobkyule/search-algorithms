from algorithms.dijkstra import dijkstra
from algorithms.astar import astar
from algorithms.simulated_annealing import simulated_annealing

import math
import random


def run_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    print("Dijkstra's shortest paths from A:", dijkstra(graph, 'A'))


def run_astar():
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
    print("A* path from A to D:", astar(graph, 'A', 'D', positions))


def run_simulated_annealing():
    def cost_fn(x): return x ** 2
    def neighbor_fn(x): return x + random.choice([-1, 1])
    def temp_fn(t): return max(0.01, min(1, 1 - math.log(t + 1) / math.log(1000)))

    best = simulated_annealing(start=10, cost_fn=cost_fn, neighbor_fn=neighbor_fn, temp_fn=temp_fn)
    print("Best solution from Simulated Annealing:", best)


if __name__ == '__main__':
    run_dijkstra()
    run_astar()
    run_simulated_annealing()