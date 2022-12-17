import string
from pathlib import Path

# priority map
priority_map = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

raw_data = Path("data.txt").read_text().splitlines()


def get_priority(row: str) -> int:
    row_length = len(row)
    # split into two

    first, second = row[: row_length // 2], row[row_length // 2 :]

    same_letters = [letter for letter in first if letter in second]
    same_letters = list(set(same_letters))

    priorities = [priority_map[letter] for letter in same_letters]

    return sum(priorities)


def part1():
    total_priority = 0
    for row in raw_data:
        total_priority += get_priority(row)
    print("Part 1:", total_priority)


def get_badge_priority(group: tuple[str]) -> int:
    one = set(group[0])
    two = set(group[1])
    three = set(group[2])

    common_letters = one.intersection(two, three)
    return sum([priority_map[letter] for letter in common_letters])


def part2():
    # group raw data into 3s
    it = iter(raw_data)
    grouped_data = list(zip(it, it, it))

    total_priority = 0
    for group in grouped_data:
        total_priority += get_badge_priority(group)
    print("Part 2:", total_priority)


part2()
