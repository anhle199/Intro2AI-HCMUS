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

# -> : one direction
# <-> : two directions
# Returns true:
#   * current node -> new node and new node is not visited
#   * there is a path from new node to current node that it is recorded
# Otherwise returns false
def is_against(adj, explored_set, parents, cur_node, new_state, src):
    if new_state in explored_set and adj[new_state][cur_node] != 0:
        return True
    if cur_node == src or new_state not in explored_set:
        return False

    node = cur_node
    while True:
        node = parents[node]
        if node == src:
            return False
        elif node == new_state:
            return True
