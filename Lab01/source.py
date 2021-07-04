from collections import deque
from heapq import *

def create_solution(parents, src, dest):
    solution = [src]
    node = dest
    while node != src:
        solution.insert(1, node)
        node = parents[node]

    return solution


def is_selected(node, explored_set, frontier):
    return (node not in explored_set) and (node not in frontier)


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
        if frontier.count == 0:
            return [[], []]  # failure

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


def find_node_in_priority_queue(q, node):
    for i in range(len(q)):
        if q[i][1] == node:
            return i
    return -1


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
        if len(frontier) == 0:
            return [[], []]  # failure

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
    # print(expanded_nodes)
    # print(path)

    # b = [
    #     [0, 4, 3, 0, 0, 0, 0],
    #     [4, 0, 0, 0, 12, 5, 0],
    #     [3, 0, 0, 7, 10, 0, 0],
    #     [0, 0, 7, 0, 2, 0, 0],
    #     [0, 12, 10, 2, 0, 0, 5],
    #     [0, 5, 0, 0, 0, 0, 16],
    #     [0, 0, 0, 0, 5, 16, 0]
    # ]
    # [expanded_nodes, path] = uniform_cost_search(b, 0, 6)
    # print(expanded_nodes)
    # print(path)

    # show output

    # save to file
    # writer = open("output.txt", "w")
    # writer.writelines([expanded_nodes, "\n" + path])
