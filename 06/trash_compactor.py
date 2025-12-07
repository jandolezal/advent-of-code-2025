"""
--- Day 6: Trash Compactor ---
https://adventofcode.com/2025/day/6
"""

import math


def load_data(filepath: str) -> tuple[list[list[int]], list[str]]:
    with open(filepath) as f:
        rows = [line.rstrip() for line in f.readlines()]

        numbers = [
            [int(num) for num in row.split(" ") if num != ""] for row in rows[:-1]
        ]
        transposed_numbers = list(map(list, zip(*numbers)))
        operation = [op for op in rows[-1].split(" ") if op != ""]

        return transposed_numbers, operation


def load_data_for_part_2(filepath: str):
    with open(filepath) as f:
        lines = [line for line in f.read().split("\n") if line != ""]
        operation = [op for op in lines[-1].split(" ") if op != ""]
        return lines[:-1], operation


def part1(data):
    all_numbers, operation = data
    operators = {
        "+": sum,
        "*": math.prod,
    }
    grand_total = 0

    for numbers, op in zip(all_numbers, operation):
        grand_total += operators[op](numbers)

    return grand_total


def part2(data):
    lines, operation = data

    rows_count = len(lines)
    cols_count = len(lines[0])

    operators = {
        "+": sum,
        "*": math.prod,
    }

    assert len(set([len(line) for line in lines])) == 1, (
        "All lines must be of equal length"
    )

    grand_total = 0
    numbers = []  # numbers within single group
    group_count = 0  # track groups of numbers to pair with correct operator
    number = ""

    for c in range(cols_count):
        for r in range(rows_count):
            number += lines[r][c]
        number = number.replace(" ", "")
        if number != "":  # new group of numbers with dedicated operator
            numbers.append(int(number))
            number = ""
        else:
            grand_total += operators[operation[group_count]](numbers)
            numbers = []
            group_count += 1
    # we would miss last group in the calculation when the for loop finishes
    grand_total += operators[operation[group_count]](numbers)
    return grand_total


test_input = load_data("06/test_input.txt")
test_result_1 = part1(test_input)
assert test_result_1 == 4277556, (
    f"Test result for part 1 should be 34277556, not {test_result_1}"
)
result_1 = part1(load_data("06/input.txt"))
print(f"Result for part 1: {result_1}")
# 4951502530386 is correct

test_input_2 = load_data_for_part_2("06/test_input.txt")
test_result_2 = part2(test_input_2)
assert test_result_2 == 3263827, (
    f"Test result for part 2 should be 3263827, not {test_result_2}"
)
result_2 = part2(load_data_for_part_2("06/input.txt"))
print(f"Result for part 2: {result_2}")
# 8486156119946 is correct
