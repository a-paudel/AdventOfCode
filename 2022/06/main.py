from pathlib import Path

data = Path("data.txt").read_text()


def check_for_distinct(data: str, number: int):
    distinct_set = []
    for i, v in enumerate(data):
        distinct_set.append(v)
        if len(distinct_set) > number:
            distinct_set.pop(0)
        if len(set(distinct_set)) == number:
            # all unique
            return i + 1


def part1():
    print("Part1: ", check_for_distinct(data, 4))


def part2():
    print("Part2: ", check_for_distinct(data, 14))


part1()
part2()
