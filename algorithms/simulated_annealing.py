def simulated_annealing(start, cost_fn, neighbor_fn, temp_fn, max_iter=1000):
    import math
    import random

    current = start
    best = start
    for t in range(1, max_iter + 1):
        T = temp_fn(t)
        if T == 0:
            break
        neighbor = neighbor_fn(current)
        delta_e = cost_fn(current) - cost_fn(neighbor)
        if delta_e > 0 or random.random() < math.exp(delta_e / T):
            current = neighbor
            if cost_fn(current) < cost_fn(best):
                best = current
    return best
