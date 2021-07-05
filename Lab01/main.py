from collections import deque
from heapq import *
from utility_functions import *

def breadth_first_search(adj, src, dest):
    count_node = len(adj)

    if count_node < 2:
        return [[], adj]

    # initialize necessary variables
    explored_set = []
    frontier = deque()  # queue: use append and popleft
    parents = {}

    # start with source node
    frontier.append(src)

    while True:
        if len(frontier) == 0:  # failure
            return [[], []]

        node = frontier.popleft()
        explored_set.append(node)

        for vertex in range(count_node):
            if (vertex != node and adj[node][vertex] != 0
                and is_selected(vertex, explored_set, frontier)):

                parents[vertex] = node
                if vertex == dest:
                    solution = create_solution(parents, src, dest)
                    return [explored_set, solution]

                frontier.append(vertex)


def uniform_cost_search(adj, src, dest):
    count_node = len(adj)

    if count_node < 2:
        return [[], adj]

    # initialize necessary variables
    explored_set = []
    frontier = []  # priority queue: use tuple with the first element is weight
    parents = {}

    # start with source node, path cost is zero
    heappush(frontier, ((0, src)))

    while True:
        if len(frontier) == 0:  # failure
            return [[], []]

        (weight, node) = heappop(frontier)
        explored_set.append(node)
        if node == dest:
            break

        for vertex in range(count_node):
            i = find_node_in_priority_queue(frontier, vertex)
            if vertex != node and adj[node][vertex] != 0:
                if vertex not in explored_set and i == -1:
                    parents[vertex] = node
                    heappush(frontier, (weight + adj[node][vertex], vertex))
                elif i != -1 and frontier[i][0] > weight + adj[node][vertex]:
                    frontier.pop(i)
                    parents[vertex] = node
                    heappush(frontier, (weight + adj[node][vertex], vertex))

    solution = create_solution(parents, src, dest)
    return [explored_set, solution]


def depth_first_search(adj, src, dest):
    count_node = len(adj)
    if count_node < 2:
        return [[], adj]

    # initialize necessary variables
    explored_set = []
    frontier = deque()  # stack: use append and pop
    parents = {}

    visited = deque()
    start_from = []
    for i in range(count_node):
        start_from.append(0)

    # start with source node
    frontier.append(src)

    while True:
        is_visited = False
        if len(frontier) == 0:
            if len(visited) == 0:
                return [[], []]
            else:  # back to old node (it is in expanded nodes)
                frontier.append(visited.pop())
                is_visited = True  # don't add old node into expanded nodes

        node = frontier.pop()
        if not is_visited:
            explored_set.append(node)

        if start_from[node] < count_node:
            visited.append(node)

            for vertex in range(start_from[node], count_node):
                if vertex != node and adj[node][vertex]:
                    if vertex == dest:
                        # explored_set.append(vertex)  # optional
                        parents[vertex] = node
                        solution = create_solution(parents, src, dest)
                        return [explored_set, solution]
                    elif not is_against(adj, explored_set, parents, node, vertex, src):
                        start_from[node] = vertex + 1
                        parents[vertex] = node
                        frontier.append(vertex)
                        break
                if vertex == count_node - 1:
                    visited.pop()
                    start_from[node] = count_node


if __name__ == "__main__":
    # read file and store
    # reader = open("input.txt", "r")
    # whole_text = reader.read()  # read whole text in input.txt file
    # lines = whole_text.split("\n")

    # call search algorithm function
    # a = [
    #     [0, 2, 0, 0, 3],
    #     [0, 0, 5, 0, 6],
    #     [0, 0, 0, 3, 0],
    #     [0, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 0],
    # ]
    # [expanded_nodes, path] = breadth_first_search(a, 0, 3)
    # [expanded_nodes, path] = uniform_cost_search(a, 0, 3)
    # [expanded_nodes, path] = depth_first_search(a, 0, 3)
    # print(expanded_nodes)
    # print(path)

    # b = [
    #     [0, 4, 3, 0, 0, 0, 0],
    #     [4, 0, 0, 0, 12, 5, 0],
    #     [3, 0, 0, 7, 10, 0, 0],
    #     [0, 0, 7, 0, 2, 0, 0],
    #     [0, 12, 10, 2, 0, 0, 5],
    #     [0, 5, 0, 0, 0, 0, 16],
    #     [0, 0, 0, 0, 5, 16, 0],
    # ]
    # [expanded_nodes, path] = breadth_first_search(b, 0, 6)
    # [expanded_nodes, path] = uniform_cost_search(b, 0, 6)
    # [expanded_nodes, path] = depth_first_search(b, 0, 6)
    # print(expanded_nodes)
    # print(path)

    # c = [
    #     [0, 4, 3, 0, 0, 0],
    #     [4, 0, 0, 0, 0, 0],
    #     [3, 0, 0, 7, 10, 0],
    #     [0, 0, 7, 0, 2, 0],
    #     [0, 12, 10, 2, 0, 5],
    #     [0, 0, 0, 0, 5, 0],
    # ]
    # [expanded_nodes, path] = breadth_first_search(c, 0, 5)
    # [expanded_nodes, path] = uniform_cost_search(c, 0, 5)
    # [expanded_nodes, path] = depth_first_search(c, 0, 5)
    # print(expanded_nodes)
    # print(path)

    # d = [
    #     [0, 2, 0, 0, 1],
    #     [0, 0, 5, 0, 6],
    #     [0, 0, 0, 3, 0],
    #     [0, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 0],
    # ]
    # [expanded_nodes, path] = depth_first_search(d, 3, 0)
    # print(expanded_nodes)
    # print(path)
    # show output

    # save to file
    # writer = open("output.txt", "w")
    # writer.writelines([expanded_nodes, "\n" + path])
