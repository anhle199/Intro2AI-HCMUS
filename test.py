a = [
    [0, 2, 0, 0, 1],
    [0, 0, 5, 0, 6],
    [0, 0, 0, 3, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]
[expanded_nodes, path] = breadth_first_search(a, 0, 3)
[expanded_nodes, path] = uniform_cost_search(a, 0, 3)
[expanded_nodes, path] = depth_first_search(a, 0, 4)
print(expanded_nodes)
print(path)

b = [
    [0, 4, 3, 0, 0, 0, 0],
    [4, 0, 0, 0, 12, 5, 0],
    [3, 0, 0, 7, 10, 0, 0],
    [0, 0, 7, 0, 2, 0, 0],
    [0, 12, 10, 2, 0, 0, 5],
    [0, 5, 0, 0, 0, 0, 16],
    [0, 0, 0, 0, 5, 16, 0],
]
hvs = [14, 12, 11, 6, 4, 11, 0]
(expanded_nodes, path) = breadth_first_search(b, 0, 6)
print(expanded_nodes)
print(path)
(expanded_nodes, path) = uniform_cost_search(b, 0, 6)
print(expanded_nodes)
print(path)
(expanded_nodes, path) = depth_first_search(b, 0, 6)
print(expanded_nodes)
print(path)
(expanded_nodes, path) = iterative_deepening_search(b, 0, 6)
print(expanded_nodes)
print(path)
(expanded_nodes, path) = greedy_best_first_search(b, hvs, 0, 6)
print(expanded_nodes)
print(path)
(expanded_nodes, path) = a_star(b, hvs, 0, 6)
print(expanded_nodes)
print(path)

c = [
    [0, 4, 3, 0, 0, 0],
    [4, 0, 0, 0, 0, 0],
    [3, 0, 0, 7, 10, 0],
    [0, 0, 7, 0, 2, 0],
    [0, 12, 10, 2, 0, 5],
    [0, 0, 0, 0, 5, 0],
]
(expanded_nodes, path) = breadth_first_search(c, 0, 5)
(expanded_nodes, path) = uniform_cost_search(c, 0, 5)
(expanded_nodes, path) = depth_first_search(c, 0, 5)
print(expanded_nodes)
print(path)

d = [
    [0, 2, 0, 0, 1],
    [0, 0, 5, 0, 6],
    [0, 0, 0, 3, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]
(expanded_nodes, path) = depth_first_search(d, 3, 0)
print(expanded_nodes)
print(path)


e = [
    [0, 2, 3, 0, 5, 0],
    [2, 0, 0, 4, 0, 0],
    [3, 0, 0, 0, 4, 0],
    [0, 4, 0, 0, 1, 2],
    [5, 0, 4, 1, 0, 5],
    [0, 0, 0, 2, 5, 0],
]
hvs1 = [5, 2, 5, 2, 1, 0]
(expanded_nodes, path) = greedy_best_first_search(e, hvs1, 0, 5)
print(expanded_nodes)
print(path)

f = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0],
]
(expanded_nodes, path) = depth_first_search(f, 0, 6)
print(expanded_nodes)
print(path)
