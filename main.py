import copy


def print_matrix(print_list):
    translation = {39: None, 44: ' ', 40: '|', 41: '|'}
    for element in print_list:
        for i in range(3):
            print(str(element[i]).translate(translation))
        print('\n')


def goal_state(data):
    if data[0][0] == ' ' and data[0][1] == 1 and data[0][2] == 2 and data[1][0] == 3 and data[1][1] == 4 and data[1][2] == 5 and data[2][0] == 6 and data[2][1] == 7 and data[2][2] == 8:
        return 1
    else:
        return 0


def possible_moves(queue_copy, visited_copy, path_copy, duplicate):
    duplicate[:] = copy.deepcopy(queue_copy.pop())
    matrix1 = copy.deepcopy(duplicate)
    convert1 = tuple(map(tuple, duplicate))  # converting matrix list to tuple for storing in hash form

    if matrix1[0][0] == ' ':
        matrix1[0][0], matrix1[0][1] = matrix1[0][1], matrix1[0][0]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[0][0], matrix1[1][0] = matrix1[1][0], matrix1[0][0]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    elif matrix1[0][1] == ' ':
        matrix1[0][0], matrix1[0][1] = matrix1[0][1], matrix1[0][0]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[0][1], matrix1[1][1] = matrix1[1][1], matrix1[0][1]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[0][1], matrix1[0][2] = matrix1[0][2], matrix1[0][1]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    elif matrix1[0][2] == ' ':
        matrix1[0][1], matrix1[0][2] = matrix1[0][2], matrix1[0][1]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[0][2], matrix1[1][2] = matrix1[1][2], matrix1[0][2]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)

    elif matrix1[1][0] == ' ':
        matrix1[1][0], matrix1[1][1] = matrix1[1][1], matrix1[1][0]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][0], matrix1[0][0] = matrix1[0][0], matrix1[1][0]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][0], matrix1[2][0] = matrix1[2][0], matrix1[1][0]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    elif matrix1[1][1] == ' ':
        matrix1[1][0], matrix1[1][1] = matrix1[1][1], matrix1[1][0]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][1], matrix1[0][1] = matrix1[0][1], matrix1[1][1]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][1], matrix1[2][1] = matrix1[2][1], matrix1[1][1]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][1], matrix1[1][2] = matrix1[1][2], matrix1[1][1]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    elif matrix1[1][2] == ' ':
        matrix1[1][1], matrix1[1][2] = matrix1[1][2], matrix1[1][1]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][2], matrix1[0][2] = matrix1[0][2], matrix1[1][2]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[1][2], matrix1[2][2] = matrix1[2][2], matrix1[1][2]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)

    elif matrix1[2][0] == ' ':
        matrix1[2][0], matrix1[1][0] = matrix1[1][0], matrix1[2][0]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[2][0], matrix1[2][1] = matrix1[2][1], matrix1[2][0]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    elif matrix1[2][1] == ' ':
        matrix1[2][0], matrix1[2][1] = matrix1[2][1], matrix1[2][0]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[2][1], matrix1[1][1] = matrix1[1][1], matrix1[2][1]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[2][1], matrix1[2][2] = matrix1[2][2], matrix1[2][1]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    elif matrix1[2][2] == ' ':
        matrix1[2][1], matrix1[2][2] = matrix1[2][2], matrix1[2][1]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
        matrix1[2][2], matrix1[1][2] = matrix1[1][2], matrix1[2][2]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1
            queue_copy.append(matrix1)
            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
    return 0


def bfs(matrix_input):
    last_popped = [[0, 0, 0], [0, ' ', 0], [0, 0, 0]]
    path = {}
    visited = []
    queue = []

    visited.append(matrix_input)
    queue.append(matrix_input)

    while queue:
        if possible_moves(queue, visited, path, last_popped) == 1:
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
    path_queue.append(copy.deepcopy(parent))

    while parent != start:
        child = copy.deepcopy(parent)
        conv3 = tuple(map(tuple, copy.deepcopy(parent)))
        parent = copy.deepcopy(path[conv3])
        path_queue.append(copy.deepcopy(child))
    path_queue.append(copy.deepcopy(parent))
    path_queue.reverse()

    print_matrix(path_queue)


print("---------- START ----------")

matrix = [[7, 2, 4], [5, ' ', 6], [8, 3, 1]]

bfs(matrix)
