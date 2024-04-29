def remove_duplicates(xs):
    zs = set()
    ys = []
    for i in xs:
        if i not in zs:
            ys.append(i)
            zs.add(i)
    return ys