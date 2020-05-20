"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20x20 grid?
"""


def print_time(runtime):
    if runtime < 0.01:
        print("Runtime: {0}ms".format(str(runtime*1000)[:5]))
    if 0.01 <= runtime <= 60:
        print("Runtime: {0}s".format(str(runtime)[:5]))
    if 60 < runtime <= 3600:
        print("Runtime: {0}m{1:02d}s".format(int(runtime / 60),
                                             int(runtime % 60)))
    if runtime > 3600:
        print("Runtime: {0}h{1:02d}m{2:02d}s".format(int(runtime / 3600),
                                                     int(runtime % 3600 / 60),
                                                     int(runtime % 60)))


def construct_graph(grid):
    """
    :param grid:  grid of things
    :return: graph of given grid
    """
    graph = {}
    for row in grid:
        for node in row:
            # ignore bottom left half
            # if node[0] > node[1]:
            #   continue

            # if case for being in the rightmost column
            if node[0]+1 < len(grid) and node[1] + 1 == len(row):
                graph[str(node)] = [[node[0] + 1, node[1]]]
                continue

            # if case for being at the bottom row
            if node[0] + 1 == len(grid) and node[1]+1 < len(row):
                graph[str(node)] = [[node[0], node[1] + 1]]
                continue

            # if case for being at any node that doesn't match the above criteria and isn't the last
            if node[0] + 1 < len(grid) and node[1] + 1 < len(row):
                graph[str(node)] = [[node[0], node[1] + 1], [node[0] + 1, node[1]]]
                continue

            # last node has only itself as connection
            # TODO remove necessity for this hacky solution
            if node == [len(grid)-1, len(row)-1]:
                graph[str(node)] = []
                continue
    return graph


def print_graph(graph):
    """
    :param graph: to print
    :return: prints all nodes
    """
    for node in graph:
        print(node, "->", graph[node], end="\n")


def find_all_paths(graph, start, end, path):
    """
    :param graph: the graph that's traversed
    :param start: starting node
    :param end: end node
    :param path: currently found paths
    :return: all possible paths
    """
    path = path + [start]
    if start == end:
        return [path]
    if str(start) not in graph or str(end) not in graph:
        return []
    paths = []
    for node in graph[str(start)]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def construct_grid(row, col):
    """
    :param row: defines the amount of rows
    :param col: defines the amount of columns
    :return: A grid that defines the lines to traverse
    """
    grid = []
    for i in range(0, row):
        tmp = []
        for j in range(0, col):
            tmp.append([i, j])
        grid.append(tmp)
    return grid


def print_grid(grid, node):
    for row in range(node[0], len(grid)):
        for col in range(node[1], len(grid[row])):
            print("{0:02d}{1:02d}".format(grid[row][col][0], grid[row][col][1]), end=" ")
        print("")


# needed for runner()
# result = 0


def runner(grid, node, rows, cols):
    """
    :param node: starting node
    :param rows: rows
    :param cols: columns
    :param grid: the grid to traverse
    :return: maximum number of possible ways
    """
    global result

    if node == [rows-1, cols-1]:
        result += 1
    if result % 1000 == 0:
        print(result, end="\r")
    for row in range(node[0], len(grid)):
        for col in range(node[1], len(grid[row])):
            return runner(grid, [row+1, col], rows, cols), runner(grid, [row, col+1], rows, cols)
    return result


def quickmafs(graph):
    """
    :param graph: takes a graph as input and weighs each vertex
    :return: maximum weight
    """
    weight = {}
    weight['[0, 0]'] = 1
    # print(graph)
    for node in graph:
        # print(node)
        for vertex in graph[node]:
            try:
                weight[str(vertex)] += weight[str(node)]
            except KeyError:
                weight[str(vertex)] = weight[str(node)]
            # print("->", vertex, weight[str(vertex)])
    return weight


def main():
    # arr = []

    i = 20
    rows = i+1
    cols = i+1
    # build grid and graph
    grid = construct_grid(rows, cols)
    graph = construct_graph(grid)

    # output both
    # print_grid(grid, [0, 0])
    # print_graph(graph)

    weight = quickmafs(graph)
    result_math = weight[str([rows-1, cols-1])]
    # paths = find_all_paths(graph, [0, 0], [i-1, i-1], [])
    # result_path = len(paths)
    # arr.append(result_path)
    # runner(grid, [0, 0], rows, cols)
    print("Problem 15: {0}".format(result_math))
    # print("Problem 15: {0}".format(result_path))

