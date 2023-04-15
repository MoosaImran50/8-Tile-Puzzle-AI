import copy


def print_matrix(print_list):
    translation = {39: None, 44: ' ', 40: '|', 41: '|'}
    for element in print_list:
        for i in range(3):
            print(str(element[i]).translate(translation))
        print('\n')


def goal_state(data):
    goal = [[1, ' ', 2],
            [3, 4, 5],
            [6, 7, 8]]
    if data == goal:
        return 1
    else:
        return 0


def find_blank(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == ' ':
                return row, col


def possible_moves(queue_copy, visited_copy, path_copy, duplicate, option):
    if option == "BFS":
        duplicate[:] = copy.deepcopy(queue_copy.pop(0))
    else:
        duplicate[:] = copy.deepcopy(queue_copy.pop())
    matrix1 = copy.deepcopy(duplicate)
    convert1 = tuple(map(tuple, duplicate))  # converting matrix list to tuple for storing in hash form

    row, col = find_blank(matrix1)

    if col > 0:
        matrix1[row][col - 1], matrix1[row][col] = matrix1[row][col], matrix1[row][col - 1]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
    if row > 0:
        matrix1[row][col], matrix1[row - 1][col] = matrix1[row - 1][col], matrix1[row][col]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
    if row < 2:
        matrix1[row][col], matrix1[row + 1][col] = matrix1[row + 1][col], matrix1[row][col]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
    if col < 2:
        matrix1[row][col + 1], matrix1[row][col] = matrix1[row][col], matrix1[row][col + 1]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)

    return 0


def bfs_dfs(matrix_input, option):
    if goal_state(matrix_input) == 1:
        print("Your input matrix is already in goal state!")
        return 1
    last_popped = []
    path = {}
    visited = []
    queue = []

    visited.append(matrix_input)
    queue.append(matrix_input)

    while queue:
        if possible_moves(queue, visited, path, last_popped, option) == 1:
            break

    conv1 = tuple(map(tuple, copy.deepcopy(visited[-1])))  # final child
    conv2 = tuple(map(tuple, copy.deepcopy(last_popped)))  # final parent
    path[conv1] = conv2

    start = tuple(map(tuple, copy.deepcopy(visited[0])))
    end = tuple(map(tuple, copy.deepcopy(visited[-1])))

    path_queue = []  # solution path from start to end
    child = end
    parent = path[child]
    path_queue.append(copy.deepcopy(child))
    moves_counter = 1

    while parent != start:
        child = copy.deepcopy(parent)
        conv3 = tuple(map(tuple, copy.deepcopy(parent)))
        parent = copy.deepcopy(path[conv3])
        path_queue.append(copy.deepcopy(child))
        moves_counter += 1
    path_queue.append(copy.deepcopy(start))
    path_queue.reverse()

    print_matrix(path_queue)
    print("Path Cost: ", moves_counter)


def get_neighbors(state, path_copy):
    neighbors = []
    duplicate = copy.deepcopy(state)
    matrix1 = copy.deepcopy(duplicate)
    convert1 = tuple(map(tuple, duplicate))  # converting matrix list to tuple for storing in hash form

    row, col = find_blank(matrix1)

    if col > 0:
        matrix1[row][col - 1], matrix1[row][col] = matrix1[row][col], matrix1[row][col - 1]  # left swap
        convert2 = tuple(map(tuple, matrix1))
        if convert2 not in path_copy:
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        neighbors.append(matrix1)
        matrix1 = copy.deepcopy(duplicate)
    if row > 0:
        matrix1[row][col], matrix1[row - 1][col] = matrix1[row - 1][col], matrix1[row][col]  # up swap
        convert2 = tuple(map(tuple, matrix1))
        if convert2 not in path_copy:
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        neighbors.append(matrix1)
        matrix1 = copy.deepcopy(duplicate)
    if row < 2:
        matrix1[row][col], matrix1[row + 1][col] = matrix1[row + 1][col], matrix1[row][col]  # down swap
        convert2 = tuple(map(tuple, matrix1))
        if convert2 not in path_copy:
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        neighbors.append(matrix1)
        matrix1 = copy.deepcopy(duplicate)
    if col < 2:
        matrix1[row][col + 1], matrix1[row][col] = matrix1[row][col], matrix1[row][col + 1]  # right swap
        convert2 = tuple(map(tuple, matrix1))
        if convert2 not in path_copy:
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        neighbors.append(matrix1)
        matrix1 = copy.deepcopy(duplicate)

    return neighbors


def ids(start_state, max_depth):
    if goal_state(start_state) == 1:
        print("Your input matrix is already in goal state!")
        return 1
    path = {}

    for depth in range(max_depth):
        visited = []
        stack = [(start_state, 0)]
        while stack:
            (current_state, current_depth) = stack.pop()
            if goal_state(current_state) == 1:
                start = tuple(map(tuple, copy.deepcopy(start_state)))
                end = tuple(map(tuple, copy.deepcopy(current_state)))

                path_queue = []  # solution path from start to end
                child = end
                parent = path[child]
                path_queue.append(copy.deepcopy(child))
                moves_counter = 1

                while parent != start:
                    child = copy.deepcopy(parent)
                    conv3 = tuple(map(tuple, copy.deepcopy(parent)))
                    parent = copy.deepcopy(path[conv3])
                    path_queue.append(copy.deepcopy(child))
                    moves_counter += 1
                path_queue.append(copy.deepcopy(start))
                path_queue.reverse()

                print_matrix(path_queue)
                print("Path Cost: ", moves_counter)
                return 1
            if current_depth < depth:
                visited.append(tuple(map(tuple, current_state)))
                for neighbor in get_neighbors(current_state, path):
                    if tuple(map(tuple, neighbor)) not in visited:
                        stack.append((neighbor, current_depth + 1))
    return 0


print("---------- START ----------")

initial_matrix = [[' ', 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]

print("---------- BFS ----------")
bfs_dfs(initial_matrix, 'BFS')

print("---------- DFS ----------")
bfs_dfs(initial_matrix, 'DFS')

print("---------- IDS ----------")
ids(initial_matrix, 200)
