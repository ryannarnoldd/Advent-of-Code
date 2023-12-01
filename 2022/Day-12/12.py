# Ryan Arnold - Advent 2022 - Day 12: ?????/
import numpy as np

#Load the data
with open("12.txt") as f:
    map = np.array([[height for height in line.strip()] for line in f])

ROWS = map.shape[0]
COLS = map.shape[1]

src = np.where(map == "S")
src = [src[0][0], src[1][0]]
end = np.where(map == "E")
end = [end[0][0], end[1][0]]

map = map.tolist()

def is_in_grid(row, col):
    return (row >= 0) and (row < ROWS) and (col >= 0) and (col < COLS)

def can_move(current, row, col):
    alphabet = "SabcdefghijklmnopqrstuvwxyzE"
    print('BBBBBBBBBBBBBBB', current)
    current = alphabet.index(current)
    next_letter = alphabet.index(map[row][col])
    return (next_letter == current + 1) or (next_letter <= current)

rowMove = [-1, 0, 0, 1]
colMove = [0, -1, 1, 0]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
queue = []
queue.append(src)
visited[src[0]][src[1]] = True
while queue:

    s = queue.pop(0)


    sX = s[0]
    sY = s[1]

    for rMove, cMove in zip(rowMove, colMove):
        newRow = s[0] + rMove
        newCol = s[1] + cMove

        if (is_in_grid(newRow, newCol) and can_move(map[sX][sY], newRow, newCol) and not visited[newRow][newCol]):
            visited[newRow][newCol] = True
            queue.append([newRow, newCol])

print(visited)


#       if pt.x == end.x and pt.y == end.y:
#         return curr.dist

#       for i in range(4):
#         row = pt.x + rowMove[i]
#         col = pt.y + colMove[i]

#         if (is_in_grid(row, col)
#               and move_to_next_cell(grid, grid[(pt.x, pt.y)], row, col)
#               and not visited[row][col]):

#           visited[row][col] = True
#           q.append(queueNode(Point(row, col), curr.dist + 1))

#     return -1 #Can't reache the destination







# def move_to_next_cell(grid, curr_letter, row, col):
#     next_letter = grid[(row, col)]
#     return (next_letter == curr_letter + 1) or (next_letter <= curr_letter)


# def breath_first_search(grid, src, end):
#     rowMove = [-1, 0, 0, 1]
#     colMove = [0, -1, 1, 0]

#     visited = [[False for _ in range(max_col)] for _ in range(max_row)]
#     visited[src.x][src.y] = True

#     q = deque()
#     qN = queueNode(src, 0)
#     q.append(qN)

#     while q:
#       curr = q.popleft()
#       pt = curr.pt

#       if pt.x == end.x and pt.y == end.y:
#         return curr.dist

#       for i in range(4):
#         row = pt.x + rowMove[i]
#         col = pt.y + colMove[i]

#         if (is_in_grid(row, col)
#               and move_to_next_cell(grid, grid[(pt.x, pt.y)], row, col)
#               and not visited[row][col]):

#           visited[row][col] = True
#           q.append(queueNode(Point(row, col), curr.dist + 1))

#     return -1 #Can't reache the destination


# #Main
# grid_map = text_to_grid(input)
# src, end = find_S_and_E(grid_map)

# S = Point(src[0], src[1])
# E = Point(end[0], end[1])

# print("Part 1 answer : ", breath_first_search(grid_map, S, E))


# def get_all_a(grid_map):
#     coord = []
#     for key, value in grid_map.items():
#       if grid_map[key] == ord("a"):
#         coord.append(key)
#     return coord


# dists = [
#     breath_first_search(grid_map, Point(a[0], a[1]), E)
#     for a in get_all_a(grid_map)
#     if breath_first_search(grid_map, Point(a[0], a[1]), E) != -1
# ]

# print("Part 2 answer : ", min(dists))

# #Timing: End
# end = time.perf_counter()
# print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")
