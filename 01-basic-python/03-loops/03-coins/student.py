def coins(one, two, five, goal):
    for i in range(one + 1):
        for j in range(two + 1):
            for o in range(five + 1):
                if i + j * 2 + o * 5 == goal:
                    return True
                else:
                    continue
    return False