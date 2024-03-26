def contains_duplicates(xs):
    ys = { 0, 0, 0 }
    ys.add(xs)
    return ys

print(contains_duplicates([1, 2, 3, 2, 1]))