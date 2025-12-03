"""
--- Day 2: Gift Shop ---
https://adventofcode.com/2025/day/2
"""


def load_data(filepath):
    with open(filepath) as f:
        return [
            tuple([int(num) for num in pair.split("-")]) for pair in f.read().split(",")
        ]


def part1(data):
    ids = []
    for start, stop in data:
        for number in range(start, stop + 1):
            id_ = str(number)
            length = len(id_)
            if length % 2 == 0:
                mid = length // 2
                left, right = id_[:mid], id_[mid:]
                if left == right:
                    ids.append(number)
    # print("ids:", ids)
    return sum(ids)


def is_id(number: int) -> int:
    """Check if the number is valid Elves gift shop ID."""
    number = str(number)
    length = len(number)
    mid = length // 2
    for slice_size in range(1, mid + 1):
        for cut in range(length // slice_size):
            slices = [number[i : i + slice_size] for i in range(0, length, slice_size)]
            if len(set(slices)) == 1:
                return True
    return False


def part2(data):
    ids = set()
    for start, stop in data:
        for number in range(start, stop + 1):
            if is_id(number):
                ids.add(number)
    return sum(ids)


test_data = load_data("02/test_input.txt")
test_result_1 = part1(test_data)
assert test_result_1 == 1227775554, (
    f"Test result for part 1 should be 1227775554, not {test_result_1}"
)

data = load_data("02/input.txt")
result_1 = part1(data)
print(result_1)
# 8576933996 is correct

test_result_2 = part2(test_data)
assert test_result_2 == 4174379265, (
    f"Test result for part 2 should be 4174379265, not {test_result_2}"
)
result_2 = part2(data)
print(result_2)
# 25663320831 is correct
