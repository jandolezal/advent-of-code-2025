"""
--- Day 3: Lobby ---
https://adventofcode.com/2025/day/3
"""


def load_data(filepath: str) -> str:
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()]


def part1(data):
    pairs = []
    for bank in data:
        numbers = []
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                numbers.append(int(bank[i] + bank[j]))
        pairs.append(max(numbers))
    # print(pairs)
    return sum(pairs)


test_input = load_data("03/test_input.txt")
test_result_1 = part1(test_input)
assert test_result_1 == 357, (
    f"Test result for part 1 should be 357, not {test_result_1}"
)
result_1 = part1(load_data("03/input.txt"))
print(f"Result for part 1: {result_1}")
# 17343 is correct
