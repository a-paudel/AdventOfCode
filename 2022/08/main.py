from pathlib import Path
import numpy as np


def parse(data: str):
    lines = data.splitlines()
    num_rows = len(lines)
    num_cols = len(lines[0].split(" "))
    char_list = [list(line) for line in lines]
    arr = np.array(char_list)
    # convert all elements to int
    arr = arr.astype(int)
    return arr


def left_elements(arr: np.ndarray, row: int, col: int):
    return arr[row, :col].tolist()


def right_elements(arr: np.ndarray, row: int, col: int):
    return arr[row, col + 1 :].tolist()


def top_elements(arr: np.ndarray, row: int, col: int):
    return arr[:row, col].tolist()


def bottom_elements(arr: np.ndarray, row: int, col: int):
    return arr[row + 1 :, col].tolist()


def top_hidden(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    elements = top_elements(arr, row, col)
    if len(elements) == 0:
        return False
    if max(elements) < current_height:
        return False
    return True


def bottom_hidden(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    elements = bottom_elements(arr, row, col)
    if len(elements) == 0:
        return False
    if max(elements) < current_height:
        return False
    return True


def left_hidden(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    elements = left_elements(arr, row, col)
    if len(elements) == 0:
        return False
    if max(elements) < current_height:
        return False
    return True


def right_hidden(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    elements = right_elements(arr, row, col)
    if len(elements) == 0:
        return False
    if max(elements) < current_height:
        return False
    return True


def part1(arr: np.ndarray):
    hidden = 0
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            if (
                top_hidden(arr, row, col)
                and bottom_hidden(arr, row, col)
                and left_hidden(arr, row, col)
                and right_hidden(arr, row, col)
            ):
                hidden += 1
    visible = arr.size - hidden
    print("Part 1:", visible)


def left_score(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    left_elements = arr[row, :col].tolist()
    left_elements.reverse()
    score = 0
    for tree_height in left_elements:
        score += 1
        if tree_height >= current_height:
            break
    return score


def right_score(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    right_elements = arr[row, col + 1 :]
    score = 0
    for tree_height in right_elements:
        score += 1
        if tree_height >= current_height:
            break
    return score


def top_score(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    top_elements = arr[:row, col].tolist()
    top_elements.reverse()
    score = 0
    for tree_height in top_elements:
        score += 1
        if tree_height >= current_height:
            break
    return score


def bottom_score(arr: np.ndarray, row: int, col: int):
    current_height = arr[row, col]
    bottom_elements = arr[row + 1 :, col]
    score = 0
    for tree_height in bottom_elements:
        score += 1
        if tree_height >= current_height:
            break
    return score


def total_score(arr: np.ndarray, row: int, col: int):
    left = left_score(arr, row, col)
    right = right_score(arr, row, col)
    top = top_score(arr, row, col)
    bottom = bottom_score(arr, row, col)
    return left * right * top * bottom


def part2(arr: np.ndarray):
    scores = []
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            scores.append(total_score(arr, row, col))
    max_score = max(scores)
    print("Part 2:", max_score)


data = Path("data.txt").read_text()
arr = parse(data)
print(arr)
part1(arr)
part2(arr)
