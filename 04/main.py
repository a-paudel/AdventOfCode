from pathlib import Path

raw_data = Path("data.txt").read_text().splitlines()


def text_to_set(text: str):
    first, last = text.split("-")
    return set(range(int(first), int(last) + 1))


def is_fully_contained(row: str):
    one_text, two_text = row.split(",")
    one_set = text_to_set(one_text)
    two_set = text_to_set(two_text)
    return one_set.issuperset(two_set) or two_set.issuperset(one_set)


def is_overlap(row: str):
    one_text, two_text = row.split(",")
    one_set = text_to_set(one_text)
    two_set = text_to_set(two_text)
    intersection = one_set.intersection(two_set)
    return bool(len(intersection))


def part1():
    total = 0
    for row in raw_data:
        if is_fully_contained(row):
            total += 1

    print("Part 1: ", total)


def part2():
    total = 0
    for row in raw_data:
        if is_overlap(row):
            total += 1

    print("Part 2: ", total)


part1()
part2()
