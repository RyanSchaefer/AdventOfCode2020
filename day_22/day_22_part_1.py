with open("day_22_input.txt", "r") as f:
    player1 = []
    player2 = []
    switch = True
    for line in f:
        if line == "Player 1:\n":
            continue
        elif line == "Player 2:\n":
            switch = False
        elif line == "\n":
            continue
        elif switch:
            player1.append(int(line.strip()))
        else:
            player2.append(int(line.strip()))
    while player1 and player2:
        if player1[0] > player2[0]:
            player1 = player1[1:] + [player1[0]] + [player2[0]]
            player2 = player2[1:]
        else:
            player2 = player2[1:] + [player2[0]] + [player1[0]]
            player1 = player1[1:]
    winner = player1 if player1 else player2
    print(winner)
    print(sum(map(lambda x: (len(winner) - x[0]) * x[1], enumerate(winner))))