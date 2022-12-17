from pathlib import Path

data = Path("data.txt").read_text()

# split data by two newlines
data_separated = data.split("\n\n")

data_total = []

for group in data_separated:
    data_list = group.splitlines()
    # convert to int
    data_list = [int(x) for x in data_list]
    total = sum(data_list)
    data_total.append(total)

# print the max value
print("part1", max(data_total))


# sort the list
data_total.sort()
# sum of top 3 values
print("part2", sum(data_total[-3:]))
