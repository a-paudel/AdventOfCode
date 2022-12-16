from pathlib import Path
import pandas as pd
import re
import numpy as np
from pprint import pprint

procedure = (
    Path("procedure.txt")
    .read_text()
    .replace("move", "")
    .replace("from", "")
    .replace("to", "")
    .splitlines()
)

raw_crates = Path("crates.txt").read_text().splitlines()


def read_crates() -> list[list[str]]:
    crates_list = []

    for line in raw_crates:
        line_list = list(line)
        # remove every 4th character
        del line_list[3::4]
        # join the list back into a string
        line = "".join(line_list)
        split = re.findall("...", line)
        crates_list.append(split)

    crates_list = np.array(crates_list).T.tolist()
    new_crates_list = []
    for row in crates_list:
        row.reverse()
        new_row = []
        for item in row:
            if item.strip() != "":
                new_row.append(item)
        new_crates_list.append(new_row)
        # print(row)

    return new_crates_list


def move_one_crate(crates: list[list[str]], before: int, after: int):
    crates[after - 1].append(crates[before - 1].pop())
    return crates


def use_procedure_1(crates: list[list[str]], amount: int, before: int, after: int):
    for i in range(amount):
        crates = move_one_crate(crates, before, after)
    return crates


def use_procedure_2(crates: list[list[str]], amount: int, before: int, after: int):
    # move the last amount items from before to after in same order
    crates[after - 1].extend(crates[before - 1][-amount:])
    # remove the last amount items from before
    del crates[before - 1][-amount:]
    return crates


# crates = use_procedure(crates, 1, 2, 1)

# pprint(crates)
def part1():
    crates = read_crates()
    for line in procedure:
        amount_str, before_str, after_str = line.strip().split()
        # convert to int
        amount = int(amount_str)
        before = int(before_str)
        after = int(after_str)
        crates = use_procedure_1(crates, amount, before, after)

    # print the last item in each row
    last_items = []
    for row in crates:
        last_items.append(row[-1])
    last_items_str = "".join(last_items)
    last_items_str = last_items_str.replace("[", "").replace("]", "")

    print(last_items_str)


def part2():
    crates = read_crates()
    for line in procedure:
        amount_str, before_str, after_str = line.strip().split()
        # convert to int
        amount = int(amount_str)
        before = int(before_str)
        after = int(after_str)
        crates = use_procedure_2(crates, amount, before, after)
    # print the last item in each row
    last_items = []
    for row in crates:
        last_items.append(row[-1])
    last_items_str = "".join(last_items)
    last_items_str = last_items_str.replace("[", "").replace("]", "")

    print(last_items_str)


part1()
part2()
