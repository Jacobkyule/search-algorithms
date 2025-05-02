# Search Algorithms in Python

---

## 👤 Student Information

**Name:** Jacob Kyule  
**Registration Number:** SCT314-C004-2676/2024

---

This repository implements:

- Dijkstra's Algorithm
- A* Search Algorithm
- Simulated Annealing

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/search-algorithms.git
cd search-algorithms
```

2. Run the main script:
```bash
python main.py
```

3. Run tests:
```bash
python -m unittest discover tests
```
✅ main.py
Purpose: This is the entry point of your program. It runs each of the three algorithms using sample data and prints the results.

When you run python main.py, it will:
Run Dijkstra's algorithm on a small graph.

Run A* algorithm on the same graph with coordinate positions.

Run Simulated Annealing to minimize the square of a number (i.e. find a value close to 0).

Expected Output Example:

Dijkstra's shortest paths from A: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
A* path from A to D: ['A', 'B', 'C', 'D']
Best solution from Simulated Annealing: 0
✅ algorithms/dijkstra.py
Purpose: Contains the implementation of Dijkstra’s Algorithm for finding the shortest paths from a starting node to all other nodes in a weighted graph.

Returns: A dictionary with the shortest distances from the start node to every other node.

✅ algorithms/astar.py
Purpose: Contains the implementation of the A Search Algorithm*. This finds the shortest path from a start node to a goal node using a heuristic (in this case, Manhattan distance based on positions).

Returns: A list of nodes showing the path from the start to the goal.

✅ algorithms/simulated_annealing.py
Purpose: Implements Simulated Annealing, a probabilistic technique for approximating the global minimum of a function.

Scenario in code: It tries to find the minimum of x^2, starting from 10.

Returns: A value close to 0, which is the minimum of the x^2 function.

✅ tests/test_dijkstra.py
Purpose: Unit test for Dijkstra’s algorithm using the same graph as in main.py.

Test: Checks that the shortest distance from A to D is 4.

✅ tests/test_astar.py
Purpose: Unit test for A* algorithm.

Test: Verifies that the computed path starts at A and ends at D.

✅ tests/test_simulated_annealing.py
Purpose: Unit test for simulated annealing.

Test: Ensures the result returned is a number (int or float) – further enhancement could verify it's close to 0.

