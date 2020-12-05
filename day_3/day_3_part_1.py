with open("day_3_input.txt", 'r') as f:
    index = 3
    count = 0
    f.__next__()
    for line in f:
        # account for newline
        count += line[index % (len(line) - 1)] == "#"
        index += 3
print(count)
