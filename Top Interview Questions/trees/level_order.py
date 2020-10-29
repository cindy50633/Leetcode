def level_order(root):
    tot_level_order = []
    node_level_dict = {root: 0}
    queue = [root]
    while queue != []:
        temp_node = queue.pop(0)
        if temp_node:
            node_level_dict[temp_node.left] = node_level_dict[temp_node] + 1
            node_level_dict[temp_node.right] = node_level_dict[temp_node] + 1
            queue.extend([temp_node.left, temp_node.right])
            try:
                tot_level_order[node_level_dict[temp_node]].append(temp_node.val)
                # sub_level_order[current_level_node_num] = temp_node.val
            except IndexError:
                tot_level_order.append([temp_node.val])
    return tot_level_order


trace = []
path = []
queue = []

def bfs(G, start):
    G.nodes_visited[start] = True
    trace.append(start)
    queue.append(start)
    while queue != []:
        temp_start = queue.pop(0)
        for neighbor in G.adj_of_node[temp_start]:
            if G.nodes_visited[neighbor] != True:
                G.nodes_visited[neighbor] = True
                trace.append(neighbor)
                queue.append(neighbor)
    return trace
