from typing import Literal
from anytree import RenderTree, NodeMixin, findall
from pathlib import Path


class FileNode(NodeMixin):
    name: str
    parent: "FileNode"
    type: str
    size: int
    children: list["FileNode"]

    def __init__(
        self, name: str, parent: "FileNode", type: Literal["file", "dir"], size: int
    ):
        self.name = name
        self.parent = parent
        self.type = type
        self.size = size


def parse_data(data: str):
    lines = data.splitlines()
    root_node = None
    current_node = None

    for line in lines:
        match line.split(" "):
            case "$", "cd", folder_name:
                if folder_name == "/":
                    root_node = FileNode(folder_name, None, "dir", 0)
                    current_node = root_node
                elif folder_name == "..":
                    current_node = current_node.parent
                else:
                    next_nodes = [
                        child
                        for child in current_node.children
                        if child.name == folder_name
                    ]
                    if len(next_nodes) == 0:
                        next_node = FileNode(folder_name, current_node, "dir", 0)
                        current_node = next_node
                        continue
                        # raise ValueError(f"Folder {folder_name} not found")
                    current_node = next_nodes[0]
            case "$", "ls":
                continue
            case "dir", folder_name:
                # create a new folder
                FileNode(folder_name, current_node, "dir", 0)
            case file_size, file_name:
                # create a new file
                FileNode(file_name, current_node, "file", int(file_size))

    return root_node


def get_dir_size(node: FileNode):
    if node.type == "file":
        return node.size
    else:
        return sum(get_dir_size(child) for child in node.children)


def part1(root_node: FileNode):
    dir_list = findall(root_node, filter_=lambda node: node.type == "dir")
    dir_sizes = [get_dir_size(dir) for dir in dir_list]
    # keep only the dirs with size <= 100000
    dir_sizes = [size for size in dir_sizes if size <= 100000]
    total = sum(dir_sizes)
    print("Part 1: ", total)
    return total


def part2(root_node: FileNode):
    dir_list = findall(root_node, filter_=lambda node: node.type == "dir")
    dir_sizes = [get_dir_size(dir) for dir in dir_list]

    total_disk = 70000000
    required_space = 30000000
    current_taken_space = get_dir_size(root_node)
    available_space = total_disk - current_taken_space
    space_to_free = required_space - available_space

    # sort the dirs by size
    dir_sizes.sort()
    # keep only the dirs with size >= space_to_free
    dir_sizes = [size for size in dir_sizes if size >= space_to_free]
    # get the minimum size
    min_size = dir_sizes[0]
    print("Part 2: ", min_size)
    return min_size


data = Path("data.txt").read_text()
root = parse_data(data)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

part1(root)
part2(root)
