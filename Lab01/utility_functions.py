def create_solution(parents, src, dest):
    solution = [src]
    if src == dest:
        return solution

    node = dest
    while node != src:
        solution.insert(1, node)
        if node not in parents.keys():
            break
        node = parents[node]

    return solution


def is_selected(node, explored_set, frontier):
    return (node not in explored_set) and (node not in frontier)


def find_node_in_priority_queue(q, node):
    for i in range(len(q)):
        if q[i][1] == node:
            return i
    return -1


def is_against(visited, explored_set, parents, src, cur_node, new_node):
    if new_node == src:
        return True
    if new_node not in explored_set:
        return False

    path = []  # path from source to current node
    if cur_node != src:
        node = cur_node
        path.append(cur_node)
        has_cycle = True
        while True:
            node = parents[node]
            path.insert(0, node)
            if node == src:
                has_cycle = False
                break
            elif node == new_node:
                break

        if has_cycle:
            return True
    else:
        path = [src]

    node = new_node
    has_cycle = True
    while True:
        if node == src:
            break

        parent = parents[node]
        if visited[node][parent] == 1 and parent in path:
            break
        if visited[node][parent] == 0:
            has_cycle = False
            break
        node = parent

    if visited[new_node][cur_node] == 0 and not has_cycle:
        return False
    return True

def parse_data(data, start_index):
    count_node = int(data[start_index])
    start_index += 1

    data[start_index] = data[start_index].split()
    src = int(data[start_index][0])
    dest = int(data[start_index][1])
    type_algo = int(data[start_index][2])
    start_index += 1

    adj = []
    for i in range(count_node):
        data[start_index] = data[start_index].split()
        adj.append([])
        for j in range(count_node):
            adj[i].append(int(data[start_index][j]))
        start_index += 1

    heuristic_values = []
    data[start_index] = data[start_index].split()
    for i in range(count_node):
        heuristic_values.append(int(data[start_index][i]))

    return (count_node, src, dest, type_algo, adj, heuristic_values)
