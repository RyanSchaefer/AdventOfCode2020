with open("day_13_input.txt", "r") as f:
    t_start = int(f.__next__().strip())
    c_time = t_start
    times = list(map(int, map(str.strip, filter(lambda x: x != "x", f.__next__().split(",")))))
    found = False
    while not found:
        for time in times:
            if c_time % time == 0:
                print(time * (c_time - t_start))
                found = True
        c_time += 1