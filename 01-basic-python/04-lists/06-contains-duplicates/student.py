def contains_duplicates(xs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j:
                if xs[i] == xs[j]:
                    return True
    return False