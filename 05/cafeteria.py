"""
--- Day 5: Cafeteria ---
https://adventofcode.com/2025/day/5
"""


def load_data(filepath: str) -> dict:
    with open(filepath) as f:
        parts = f.read().split("\n\n")
        top = [
            tuple([int(item) for item in line.split("-")]) for line in parts[0].split()
        ]
        bottom = [int(item) for item in parts[1].split()]
        return {"ranges": top, "ids": bottom}


def part1(data):
    count = 0
    for id_ in data["ids"]:
        for start, stop in data["ranges"]:
            if start <= id_ <= stop:
                count += 1
                break
    return count


def part2(data):
    ranges = sorted(data["ranges"], key=lambda x: x[0])

    merged_ranges = []
    for start, stop in ranges:
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], stop))
        else:
            merged_ranges.append((start, stop))

    count = 0
    for start, stop in merged_ranges:
        count += stop - start + 1

    return count


test_input = load_data("05/test_input.txt")
test_result_1 = part1(test_input)
assert test_result_1 == 3, f"Test result for part 1 should be 3, not {test_result_1}"
result_1 = part1(load_data("05/input.txt"))
print(f"Result for part 1: {result_1}")
# 733 is correct

test_result_2 = part2(test_input)
assert test_result_2 == 14, f"Test result for part 2 should be 14, not {test_result_2}"
result_2 = part2(load_data("05/input.txt"))
print(f"Result for part 2: {result_2}")
# 7381403408525 is not correct
# 345821388687084 is correct
