"""
--- Day 9: Movie Theater ---
https://adventofcode.com/2025/day/9
"""

from itertools import combinations


def load_data(filepath: str):
    with open(filepath) as f:
        return [
            tuple([int(num) for num in line.strip().split(",")])
            for line in f.readlines()
        ]


def part1(data):
    area = 0
    for (x1, y1), (x2, y2) in combinations(data, 2):
        candidate_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if candidate_area > area:
            area = candidate_area

    return area


def part2(data):
    return


test_input = load_data("09/test_input.txt")
test_result_1 = part1(test_input)
assert test_result_1 == 50, f"Test result for part 1 should be 50, not {test_result_1}"
result_1 = part1(load_data("09/input.txt"))
print(f"Result for part 1: {result_1}")
# 4776100539 is correct

test_input_2 = load_data("09/test_input.txt")
test_result_2 = part2(test_input_2)
assert test_result_2 == 24, f"Test result for part 2 should be 24, not {test_result_2}"
result_2 = part2(load_data("09/input.txt"))
print(f"Result for part 2: {result_2}")
#
