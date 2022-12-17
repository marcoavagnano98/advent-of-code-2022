if __name__ == '__main__':
    total_trees = 0
    ind = 0

    with open("eight/input.txt", "r") as fl:
        grid = [list(map(int, line)) for line in fl.read().splitlines()]
        all_scenic = []
        counter = 0
        for row in range(len(grid)):

            for column in range(len(grid[row])):

                if all(grid[row][column] > grid[row][elem] for elem in range(column)) or all(
                        grid[row][column] > grid[row][elem] for elem in range(column + 1, len(grid))) \
                        or all(grid[row][column] > grid[elem][column] for elem in range(row + 1, len(grid))) or all(
                    grid[row][column] > grid[elem][column] for elem in range(row)):
                    counter += 1

                if 0 < row < len(grid) - 1 and 0 < column < len(grid) - 1:
                    # check left
                    count_left = 0
                    for i in range(column - 1, -1, -1):
                        if grid[row][i] < grid[row][column]:
                            count_left += 1
                            continue
                        break
                    # check right
                    count_right = 0
                    for i in range(column + 1, len(grid[row])):
                        if grid[row][i] < grid[row][column]:
                            count_right += 1
                            continue
                        break
                    # check up
                    count_up = 0
                    for i in range(row - 1, -1, -1):
                        if grid[i][column] < grid[row][column]:
                            count_up += 1
                            continue
                        break
                    # check down
                    count_down = 0
                    for i in range(row + 1, len(grid)):
                        if grid[i][column] < grid[row][column]:
                            count_down += 1
                            continue
                        break
                    # if matrix elem is bigger than all remaining elem on left/right/up/down counter will not be
                    # incremented
                    all_scenic.append((count_down + 1 if (row + count_down) < len(grid) - 1 else count_down) * (
                        count_right + 1 if (column + count_right) < len(grid) - 1 else count_right) * (
                                          count_left + 1 if column - count_left > 0 else count_left) * (
                                          count_up + 1 if (row - count_up) > 0 else count_up))
        print(f'All visible trees: {counter}, Max scenic point: {max(all_scenic)}')
