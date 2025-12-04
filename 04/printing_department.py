"""
Day 4: Printing Department ---
https://adventofcode.com/2025/day/4
"""


def load_data(
    filepath: str,
) -> list[list[str]]:  # list of rows, each row is a list of "@" or "."
    with open(filepath) as f:
        return [[char for char in line.strip()] for line in f.readlines()]


def check_neighbours(grid, row, col, treshold=4) -> bool:
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    count = 0

    for rd, cd in directions:
        new_row, new_col = row + rd, col + cd
        # do not end up outside the grid
        if (0 <= new_row < rows) and (0 <= new_col < cols):
            if grid[new_row][new_col] == "@":
                count += 1
    if count < treshold:
        return True

    return False


def part1(data):
    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "@":  # check only "@" positions
                if check_neighbours(data, r, c):
                    count += 1
    return count


def check_grid_once(grid) -> list[tuple[int, int]]:
    rolls_to_remove_positions = []

    # Check all positions in the current state of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":  # check only "@" positions
                # can we remove this roll?
                if check_neighbours(grid, r, c):
                    rolls_to_remove_positions.append((r, c))

    return rolls_to_remove_positions


def part2(data):
    count = 0
    dry_run = False

    while not dry_run:
        # Remove rolls at collected positions
        rolls_to_remove_positions = check_grid_once(data)

        # Mutate state of the grid
        if not rolls_to_remove_positions:
            dry_run = True
        else:
            count += len(rolls_to_remove_positions)
            for r, c in rolls_to_remove_positions:
                data[r][c] = "."

    return count


test_input = load_data("04/test_input.txt")
test_result_1 = part1(test_input)
assert test_result_1 == 13, f"Test result for part 1 should be 13, not {test_result_1}"
result_1 = part1(load_data("04/input.txt"))
print(f"Result for part 1: {result_1}")
# 1551 is correct

test_result_2 = part2(test_input)
assert test_result_2 == 43, f"Test result for part 2 should be 43, not {test_result_2}"
result_2 = part2(load_data("04/input.txt"))
print(f"Result for part 2: {result_2}")
# 9784 is correct
