import copy
import heapq


goal_matrix = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]


def print_matrix(print_list):
    translation = {39: None, 44: ' ', 40: '|', 41: '|'}
    for element in print_list:
        for i in range(3):
            print(str(element[i]).translate(translation))
        print('\n')


def goal_state(data):
    if data == goal_matrix:
        return 1
    else:
        return 0


def find_blank(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                for a in range(3):
                    for b in range(3):
                        if goal_matrix[a][b] == state[i][j]:
                            row, col = a, b
                            distance += abs(i - row) + abs(j - col)
    return distance


def possible_moves(queue_copy, visited_copy, path_copy, duplicate, option):
    key, value = heapq.heappop(queue_copy)
    current_state = 0
    height = 0

    if option == "BFS":
        current_state = value
    else:
        current_state, height = value

    duplicate[:] = copy.deepcopy(current_state)
    matrix1 = copy.deepcopy(duplicate)
    convert1 = tuple(map(tuple, duplicate))  # converting matrix list to tuple for storing in hash form

    row, col = find_blank(matrix1)

    if col > 0:
        matrix1[row][col - 1], matrix1[row][col] = matrix1[row][col], matrix1[row][col - 1]  # left swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1

            if option == "BFS":
                heapq.heappush(queue_copy, (manhattan_distance(matrix1), matrix1))
            else:
                heapq.heappush(queue_copy, (manhattan_distance(matrix1) + height + 1, (matrix1, height + 1)))

            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
    if row > 0:
        matrix1[row][col], matrix1[row - 1][col] = matrix1[row - 1][col], matrix1[row][col]  # up swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1

            if option == "BFS":
                heapq.heappush(queue_copy, (manhattan_distance(matrix1), matrix1))
            else:
                heapq.heappush(queue_copy, (manhattan_distance(matrix1) + height + 1, (matrix1, height + 1)))

            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
    if row < 2:
        matrix1[row][col], matrix1[row + 1][col] = matrix1[row + 1][col], matrix1[row][col]  # down swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1

            if option == "BFS":
                heapq.heappush(queue_copy, (manhattan_distance(matrix1), matrix1))
            else:
                heapq.heappush(queue_copy, (manhattan_distance(matrix1) + height + 1, (matrix1, height + 1)))

            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)
    if col < 2:
        matrix1[row][col + 1], matrix1[row][col] = matrix1[row][col], matrix1[row][col + 1]  # right swap
        if matrix1 not in visited_copy:
            visited_copy.append(matrix1)
            if goal_state(matrix1) == 1:
                return 1

            if option == "BFS":
                heapq.heappush(queue_copy, (manhattan_distance(matrix1), matrix1))
            else:
                heapq.heappush(queue_copy, (manhattan_distance(matrix1) + height + 1, (matrix1, height + 1)))

            convert2 = tuple(map(tuple, matrix1))
            path_copy[copy.deepcopy(convert2)] = copy.deepcopy(convert1)
        matrix1 = copy.deepcopy(duplicate)

    return 0


def bfs(matrix_input, option):
    if goal_state(matrix_input) == 1:
        print("Your input matrix is already in goal state!")
        return 1
    last_popped = []
    path = {}
    visited = []
    queue = []

    height = 0
    f = 0

    if option == "BFS":
        heapq.heappush(queue, (f, matrix_input))
    else:
        heapq.heappush(queue, (f, (matrix_input, height)))
    visited.append(matrix_input)

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


print("---------- START ----------")

initial_matrix = [[7, 2, 4],
                  [5, 0, 6],
                  [8, 3, 1]]

print("---------- BFS ----------")
bfs(initial_matrix, 'BFS')

print("---------- A* ----------")
bfs(initial_matrix, 'A*')
