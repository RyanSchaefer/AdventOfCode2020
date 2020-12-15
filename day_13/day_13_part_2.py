with open("day_13_input.txt", 'r') as f:
    f.__next__()
    times = [int(x) if x != "x" else x for x in f.__next__().strip().split(",")]
    print(", ".join([f"(t + {offset}) mod {time} = 0" for offset, time in enumerate(times) if time != "x"]))
