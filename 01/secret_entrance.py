"""
--- Day 1: Secret Entrance ---
https://adventofcode.com/2025/day/1
"""


def load_data(filepath):
    with open(filepath) as f:
        data = []
        for line in f.readlines():
            row = line.strip()
            data.append((row[0], int(row[1:])))
    return data


def part1(data):
    current_step = 50
    times_at_zero = 0

    for direction, steps in data:
        if direction == "R":
            current_step = (current_step + steps) % 100
        else:
            current_step = (current_step - steps) % 100

        if current_step == 0:
            times_at_zero += 1

    return times_at_zero


def part2(data):
    current_step = 50
    times_at_zeros = 0

    for direction, steps in data:
        if direction == "L":
            times_at_zeros += steps // 100
            steps = steps % 100
            if current_step and current_step <= steps:
                times_at_zeros += 1
            current_step -= steps
        else:
            current_step += steps
            times_at_zeros += current_step // 100
        current_step = current_step % 100

    return times_at_zeros


test_data = load_data("01/test_input.txt")
test_result_1 = part1(test_data)
assert test_result_1 == 3, f"Test result for part 1 should be 3, not {test_result_1}"

result_1 = part1(load_data("01/input.txt"))
print(result_1)
# 1011 is correct

test_result_2 = part2(test_data)
assert test_result_2 == 6, f"Test result for part 2 should be 6, not {test_result_2}"

result_2 = part2(load_data("01/input.txt"))
print(result_2)
# 5967 high
# 4877 low
# 5340 wrong
# 5937 is correct (stuck with L directions)
