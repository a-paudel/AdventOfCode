#%%
from pathlib import Path
from typing import Literal

#%%
data = Path("data.txt").read_text()
#%%
def move_head_one_step(
    current_pos: tuple[int, int], direction: Literal["R", "L", "U", "D"]
):
    match direction:
        case "R":
            new_pos = (current_pos[0] + 1, current_pos[1])
        case "L":
            new_pos = (current_pos[0] - 1, current_pos[1])
        case "U":
            new_pos = (current_pos[0], current_pos[1] + 1)
        case "D":
            new_pos = (current_pos[0], current_pos[1] - 1)

    return new_pos


def calculate_tail_position(
    current_head_pos: tuple[int, int], current_tail_pos: tuple[int, int]
):
    # if tail is adjacent to head in any direction, return current_head_pos
    x_diff = current_head_pos[0] - current_tail_pos[0]
    y_diff = current_head_pos[1] - current_tail_pos[1]

    # if adjacent, return current pos
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return current_tail_pos

    # straight movement
    if x_diff == 0:
        # move tail up or down
        if y_diff > 0:
            new_pos = (current_tail_pos[0], current_tail_pos[1] + 1)
        else:
            new_pos = (current_tail_pos[0], current_tail_pos[1] - 1)
    elif y_diff == 0:
        # move tail left or right
        if x_diff > 0:
            new_pos = (current_tail_pos[0] + 1, current_tail_pos[1])
        else:
            new_pos = (current_tail_pos[0] - 1, current_tail_pos[1])

    # diagonal movement
    elif x_diff != 0 and y_diff != 0:
        if y_diff > 0 and x_diff > 0:
            new_pos = (current_tail_pos[0] + 1, current_tail_pos[1] + 1)
        elif y_diff > 0 and x_diff < 0:
            new_pos = (current_tail_pos[0] - 1, current_tail_pos[1] + 1)
        elif y_diff < 0 and x_diff > 0:
            new_pos = (current_tail_pos[0] + 1, current_tail_pos[1] - 1)
        elif y_diff < 0 and x_diff < 0:
            new_pos = (current_tail_pos[0] - 1, current_tail_pos[1] - 1)

    return new_pos


#%%
def part1():
    start_pos = (0, 0)
    head_pos = start_pos
    tail_pos = start_pos
    tail_positions: list[tuple[int, int]] = []
    for line in data.splitlines():
        direction, distance_str = line.split(" ")
        distance = int(distance_str)

        for _ in range(distance):
            new_head_pos = move_head_one_step(head_pos, direction)
            new_tail_pos = calculate_tail_position(new_head_pos, tail_pos)
            tail_positions.append(new_tail_pos)
            head_pos = new_head_pos
            tail_pos = new_tail_pos

    num_tail_positions = len(set(tail_positions))
    print(f"Part 1: {num_tail_positions}")


part1()

#%%
def part2():
    start_pos = (0, 0)
    initial_knot_positions = [
        start_pos,  # head
        start_pos,
        start_pos,
        start_pos,
        start_pos,
        start_pos,
        start_pos,
        start_pos,
        start_pos,
        start_pos,  # tail
    ]
    knot_positions = initial_knot_positions.copy()
    tail_positions: list[tuple[int, int]] = []
    for line in data.splitlines():
        direction, distance_str = line.split(" ")
        distance = int(distance_str)

        for _ in range(distance):
            knot_positions[0] = move_head_one_step(knot_positions[0], direction)
            # for each knot apart from the head knot, calculate new position
            for i in range(1, len(knot_positions)):
                knot_positions[i] = calculate_tail_position(
                    knot_positions[i - 1], knot_positions[i]
                )
                # if its the tail knot, add to tail_positions
                if i == len(knot_positions) - 1:
                    tail_positions.append(knot_positions[i])

    num_tail_positions = len(set(tail_positions))
    print(f"Part 2: {num_tail_positions}")


part2()
