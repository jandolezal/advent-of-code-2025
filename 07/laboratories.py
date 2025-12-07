"""
--- Day 6: Trash Compactor ---
https://adventofcode.com/2025/day/6
"""


def load_data(filepath: str):
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()]


def part1(data):
    width = len(data[0])
    count = 0

    beams = set()  # initialize set of beams columns
    beams.add(data[0].find("S"))

    for r, row in enumerate(data[1:], start=1):
        # check for splitters and update beams positions
        splitters = [c for c, char in enumerate(row) if char == "^"]
        temp_beams = set()

        for splitter in splitters:
            # is there a beam from the past on splitter position?
            if splitter in beams:
                count += 1
                if splitter - 1 >= 0:
                    temp_beams.add(splitter - 1)
                if splitter + 1 < width:
                    temp_beams.add(splitter + 1)
                # beam stops on splitter, new beams were created left and right
                beams.remove(splitter)

        # update beams columns tracking set
        beams = {*beams, *temp_beams}

    return count


def part2(data):
    return


test_input = load_data("07/test_input.txt")
test_result_1 = part1(test_input)
assert test_result_1 == 21, f"Test result for part 1 should be 21, not {test_result_1}"
result_1 = part1(load_data("07/input.txt"))
print(f"Result for part 1: {result_1}")
# 1687 is correct

test_input_2 = load_data("07/test_input.txt")
test_result_2 = part2(test_input_2)
assert test_result_2 == 40, f"Test result for part 2 should be 40, not {test_result_2}"
result_2 = part2(load_data("07/input.txt"))
print(f"Result for part 2: {result_2}")
#
