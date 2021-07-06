from collections import deque
from heapq import *
from utility_functions import *


CUTOFF = "CUTOFF"


def breadth_first_search(adj, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return ([], adj)

    # initialize necessary variables
    explored_set = []
    frontier = deque()  # queue: use append and popleft
    parents = {}

    # start with source node
    frontier.append(src)

    while True:
        if len(frontier) == 0:  # failure
            return (explored_set, [])

        node = frontier.popleft()
        explored_set.append(node)

        for vertex in range(count_node):
            if (vertex != node and adj[node][vertex] != 0
                and is_selected(vertex, explored_set, frontier)):

                parents[vertex] = node
                if vertex == dest:
                    solution = create_solution(parents, src, dest)
                    return (explored_set, solution)

                frontier.append(vertex)


def recur_depth_first_search(visited, explored_set, parents, src, dest, cur):
    if cur == dest:
        return (visited, explored_set, parents, create_solution(parents, src, dest))

    count_node = len(visited)
    explored_set.append(cur)
    solution = []

    for vertex in range(count_node):
        if vertex != cur and visited[cur][vertex] == 1:
            if not is_against(visited, explored_set, parents, src, cur, vertex):
                visited[cur][vertex] = 0
                temp = visited[vertex][cur]
                visited[vertex][cur] = 0
                parents[vertex] = cur

                (visited, explored_set, parents, solution) = recur_depth_first_search(visited, explored_set, parents, src, dest, vertex)

                visited[cur][vertex] = 1
                visited[vertex][cur] = temp

                if solution != []:
                    break

    return (visited, explored_set, parents, solution)


def depth_first_search(adj, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return ([], adj)

    # initialize necessary variables
    explored_set = []
    parents = {}

    visited = adj
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] != 0:
                visited[i][j] = 1

    (visited, explored_set, parents, solution) = recur_depth_first_search(visited, explored_set, parents, src, dest, src)
    return (explored_set, solution)


def uniform_cost_search(adj, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return ([], adj)

    # initialize necessary variables
    explored_set = []
    frontier = []  # priority queue: use tuple with the first element is weight
    parents = {}

    # start with source node, path cost is zero
    heappush(frontier, ((0, src)))

    while True:
        if len(frontier) == 0:  # failure
            return (explored_set, [])

        (weight, node) = heappop(frontier)
        explored_set.append(node)
        if node == dest:
            break

        for vertex in range(count_node):
            weight_new_node = weight + adj[node][vertex]
            i = find_node_in_priority_queue(frontier, vertex)
            if vertex != node and adj[node][vertex] != 0:
                if vertex not in explored_set and i == -1:
                    parents[vertex] = node
                    heappush(frontier, (weight_new_node, vertex))
                elif i != -1 and frontier[i][0] > weight_new_node:
                    frontier.pop(i)
                    parents[vertex] = node
                    heappush(frontier, (weight_new_node, vertex))

    solution = create_solution(parents, src, dest)
    return (explored_set, solution)


def depth_limited_search(adj, src, dest, limit):
    explored_set = []
    parents = {}
    visited = adj

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] != 0:
                visited[i][j] = 1

    result = recur_dls(visited, src, dest, limit, src, explored_set, parents)
    return (result[1], result[3])  # (explored_set, solution)


def recur_dls(visited, src, dest, limit, node, explored_set, parents):
    if node == dest:
        explored_set.append(node)
        return (visited, explored_set, parents, create_solution(parents, src, dest))
    if limit == 0:
        explored_set.append(node)
        return (visited, explored_set, parents, CUTOFF)

    cutoff_occurred = False
    count_node = len(visited)
    solution = []

    explored_set.append(node)
    for vertex in range(count_node):
        if vertex != node and visited[node][vertex] == 1:
            visited[node][vertex] = 0
            temp = visited[vertex][node]
            visited[vertex][node] = 0
            parents[vertex] = node

            (visited, explored_set, parents, solution) = recur_dls(visited, src, dest, limit - 1, vertex, explored_set, parents)

            visited[node][vertex] = 1
            visited[vertex][node] = temp

            if solution == CUTOFF:
                cutoff_occurred = True
            elif solution != []:
                return (visited, explored_set, parents, create_solution(parents, src, dest))

    if cutoff_occurred:
        return (visited, explored_set, parents, CUTOFF)
    return (visited, explored_set, parents, [])


def iterative_deepening_search(adj, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return [[], adj]

    # initialize necessary variables
    explored_sets = []
    limit = 0

    while True:
        (explored_set, solution) = depth_limited_search(adj, src, dest, limit)
        limit += 1
        explored_sets.append(explored_set)
        if solution != CUTOFF:
            return (explored_sets, solution)


def greedy_best_first_search(adj, heuristic_values, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return ([], adj)

    # initialize necessary variables
    explored_set = []
    frontier = []  # priority queue: use tuple with the first element is heuristic_val
    parents = {}

    # start with source node, path cost is zero
    heappush(frontier, ((heuristic_values[src], src)))

    while True:
        if len(frontier) == 0:  # failure
            return (explored_set, [])

        (heuristic_val, node) = heappop(frontier)
        if node == dest:
            break

        explored_set.append(node)
        for vertex in range(count_node):
            i = find_node_in_priority_queue(frontier, vertex)
            if vertex != node and adj[node][vertex] != 0:
                if vertex not in explored_set and i == -1:
                    parents[vertex] = node
                    heappush(frontier, (heuristic_values[vertex], vertex))

    solution = create_solution(parents, src, dest)
    return (explored_set, solution)


def a_star(adj, heuristic_values, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return ([], adj)

    # initialize necessary variables
    explored_set = []
    frontier = []  # priority queue: use tuple with the first element is heuristic_val
    parents = {}

    # start with source node, path cost is zero
    heappush(frontier, ((heuristic_values[src], src)))

    while True:
        if len(frontier) == 0:  # failure
            return (explored_set, [])

        (cost, node) = heappop(frontier)
        explored_set.append(node)
        if node == dest:
            break

        cost -= heuristic_values[node]
        for vertex in range(count_node):
            cost_new_node = heuristic_values[vertex] + adj[node][vertex] + cost
            i = find_node_in_priority_queue(frontier, vertex)
            if vertex != node and adj[node][vertex] != 0:
                if vertex not in explored_set and i == -1:
                    parents[vertex] = node
                    heappush(frontier, (cost_new_node + cost, vertex))
                elif i != -1 and frontier[i][0] > cost_new_node:
                    frontier.pop(i)
                    parents[vertex] = node
                    heappush(frontier, (cost_new_node, vertex))

    solution = create_solution(parents, src, dest)
    return (explored_set, solution)


def search_algorithm(adj, heuristic_values, src, dest, type_algo):
    switcher = {
        0: breadth_first_search(adj, src, dest),
        1: depth_first_search(adj, src, dest),
        2: uniform_cost_search(adj, src, dest),
        3: iterative_deepening_search(adj, src, dest),
        4: greedy_best_first_search(adj, heuristic_values, src, dest),
        5: a_star(adj, heuristic_values, src, dest),
        # 6: 
    }

    return switcher.get(type_algo, ([], []))


if __name__ == "__main__":
    # read file and store
    # reader = open("input.txt", "r")
    # whole_text = reader.read()  # read whole text in input.txt file
    # lines = whole_text.split("\n")
    # reader.close()

    # writer = open("output.txt", "w")
    # i = 0
    # while i < len(lines):
    #     count_node = int(lines[i])
    #     i += 1

    #     lines[i] = lines[i].split()
    #     src = int(lines[i][0])
    #     dest = int(lines[i][1])
    #     type_algo = int(lines[i][2])
    #     i += 1

    #     adj = []
    #     for j in range(count_node):
    #         lines[i] = lines[i].split()
    #         adj.append([])
    #         for k in range(count_node):
    #             adj[j].append(int(lines[i][k]))
    #         i += 1

    #     heuristic_values = []
    #     lines[i] = lines[i].split()
    #     for j in range(count_node):
    #         heuristic_values.append(int(lines[i][j]))
    #     i += 1

    #     (expanded_nodes, path) = search_algorithm(adj, heuristic_values, src, dest, type_algo)
    #     first_line = " ".join(map(str, expanded_nodes))
    #     second_line = "No path."
    #     if path != []:
    #         second_line = " ".join(map(str, path))

    #     writer.writelines([first_line + "\n", second_line + "\n"])

    # writer.close()
